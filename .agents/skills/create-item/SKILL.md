---
name: create-item
description: Cria a estrutura e contexto inicial para um novo item raiz na pasta Ativo/, suportando os tipos projeto, produto e estudo.
---

# Habilidade: Criar Novo Item

Esta habilidade orienta o subagente agy a estruturar um novo item raiz (projeto, produto ou estudo principal) no cofre com as seções e propriedades corretas. Para definições detalhadas de cada tipo e papel operacional, consulte o [glossário de tipos](.agents/assistant/glossary.md).

## Diretrizes de Execução

Quando solicitado a criar um item (ex: *"Crie o projeto Nome"*, *"Crie o estudo Nome"*, *"Crie o produto Nome"*):

1. **Determinação do Tipo:** Identifique o tipo do item a partir do contexto do usuário:
   *   `projeto` — Iniciativas com escopo, cronograma e entregas definidos.
   *   `produto` — Ferramentas, sistemas ou artefatos mantidos continuamente.
   *   `estudo` — Temas de aprendizado, pesquisa ou exploração conceitual.
   Se o tipo não for claro pelo contexto, pergunte ao usuário.
2. **Definição de Nome e Descrição:** Obtenha o nome e o contexto/descrição do item a partir da solicitação do usuário.
3. **Higienização do Nome:** Crie um nome de arquivo seguro a partir do nome do item (ex: `Meu Novo Projeto.md`).
4. **Verificação de Duplicatas:** Verifique se o item já existe em `Ativo/` ou `Arquivo/`. Se sim, avise o usuário e encerre a operação.
5. **Determinação do Domínio:** Identifique se o item é de trabalho (`area/evo`), freelance (`area/freelance`) ou pessoal (`area/pessoal`). Se não for claro pelo contexto, pergunte ao usuário. O domínio é registrado como tag, não como property.
6. **Determinação do Status:** Identifique o status inicial a partir do contexto do usuário:
   *   `planejado` — standby, sondagem, rascunho, "para não perder a ideia".
   *   `em-andamento` — priorizado, ativo, o usuário disse que vai trabalhar nele.
7. **Metadados (Obsidian Properties):** Adicione o cabeçalho YAML frontmatter moderno:
   ```yaml
   ---
   created: AAAA-MM-DD
   type: projeto # ou produto, estudo
   status: planejado # ou em-andamento
   description: "Resumo gerado a partir do contexto do usuário"
   tags:
     - status/planejado
     - area/evo # area/evo, area/freelance ou area/pessoal
     - papel/raiz
   links: [] # adicione links para notas existentes se forem citadas
   ---
   ```
8. **Estrutura do Conteúdo (adaptativa por tipo e status):**

   **Secoes obrigatorias (todos os tipos e status):**
   *   `# [Nome do Item]`
   *   `## Objetivo e Impacto` (breve: qual o objetivo claro).
   *   `## Motivacao e Origem` (o que aconteceu que disparou o item — qual evento, demanda ou conversa originou a ideia, com wikilink para a nota diária de origem, ex: `[[DD-MM-YYYY]]`).
   *   `## Escopo e Contexto` (descrição do que se sabe até o momento. **NÃO inventar escopo** além do que o usuário informou).
   *   `## Diario de Bordo` (entrada inicial registrando a criação).

   **Secoes adicionais por tipo e status:**

   | Tipo | Status | Secao adicional | Conteudo |
   |---|---|---|---|
   | `projeto` | `planejado` | `## Discovery e Questoes Abertas` | Perguntas pendentes, dependências, itens de sondagem (ex: `- [ ] Aguardar retorno de X`). |
   | `projeto` | `em-andamento` | `## Cronograma e Marcos` | Lista de checkboxes `- [ ]` com entregas definidas pelo usuário. |
   | `produto` | `planejado` | `## Discovery e Questoes Abertas` | Perguntas pendentes, dependências, itens de sondagem. |
   | `produto` | `em-andamento` | `## Cronograma e Marcos` + `## Melhorias Futuras` | Lista de entregas + lista de melhorias e evoluções futuras. |
   | `estudo` | qualquer | `## Conceitos e Referencias` | Links estilo MOC, conceitos-chave, referências bibliográficas. |

   > **REGRA:** Itens com status `planejado` **NÃO** possuem `Cronograma e Marcos`. Não invente tarefas de execução para itens que o usuário não priorizou.

9. **Gravação:** Salve o arquivo no diretório `Ativo/` apenas quando for `papel/raiz`. Se o usuário pedir um dossiê, sub-hub, artefato de apoio ou nota subordinada a outro item, salve em `Arquivo/` com `papel/filha` e link para a raiz correspondente.
10. **Atualizações de Índices, Diário e Logs:**
    *   Se for `papel/raiz`, insira a nota na seção correspondente do `index.md` adicionando a descrição inline para Progressive Disclosure (ex: `- [[Nome do Item]] — [status] — [description]`). Notas `papel/filha` não entram no `index.md`; elas devem ser linkadas no corpo da nota raiz.
    *   Localize a nota diária do dia atual em `Diario/Daily/DD-MM-YYYY.md` (se não existir, crie-a baseada no template). Na seção `# Notas`, adicione a linha:
        `- **Novo [Tipo]**: Criado o [tipo] [[Nome do Item]] com status [status].` 
        *(ex: `- **Novo Projeto**: Criado o projeto [[Verificador de Tags de API no Azure]] com status planejado.*)*
    *   Registre o evento silenciosamente no `.agents/assistant/logs.md` (ex: `## [AAAA-MM-DD] create-item | Criado novo [tipo] "[Nome do Item]"`).

