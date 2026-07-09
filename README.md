# Segundo Cérebro (LLM Wiki) — Guia de Uso do Projeto

Este repositório é um **Segundo Cérebro (LLM Wiki)** estruturado para funcionar como base de conhecimento pessoal e gerenciador de produtividade. Ele foi projetado para ser usado no **Obsidian** e é copiloto pelo assistente de Inteligência Artificial **agy** (rodando originalmente na plataforma Antigravity e compatível com Codex via `AGENTS.md`).

O objetivo deste projeto é equilibrar a captura ágil de ideias com a organização estruturada e de longo prazo de projetos, produtos, estudos e tarefas, utilizando um modelo de camadas e automações inteligentes baseadas em IA.

---

## 📂 Estrutura de Pastas (O Modelo de 5 Camadas)

O cofre é organizado em camadas lógicas para garantir a integridade dos dados e otimizar o fluxo de trabalho do assistente de IA e do usuário:

| Camada | Pasta | Nome Lógico | Descrição e Uso |
| :--- | :--- | :--- | :--- |
| **Camada 0** | `Inbox/` | Buffer Temporário | Ponto de entrada rápido. Rascunhos, capturas rápidas ou notas cruas (criadas por você ou pelo assistente via skill `capture-idea`). É limpa e classificada periodicamente. |
| **Camada 1** | `Fontes/` | Fontes Imutáveis | Arquivo de documentos originais (artigos salvos, PDFs, imagens, logs originais). Uma vez processados na Inbox, os arquivos brutos originais vêm para cá. O assistente lê esta pasta para referência, mas nunca altera ou exclui seus arquivos. |
| **Camada 2** | `Ativo/` | Painel Ativo | Itens raiz acompanháveis (`papel/raiz`) que devem aparecer no painel de decisão: projetos, produtos e estudos principais. Também contém `Ativo/backlog.md`. |
| **Camada 2** | `Diario/` | Diário Temporal | Contém as notas diárias localizadas em `Diario/Daily/` (no formato `DD-MM-YYYY.md`). É o seu painel diário de tarefas e notas soltas. |
| **Camada 3** | `.agents/` + `AGENTS.md` | Esquema e Regras | Arquivos de configuração, manuais de conduta e as **Skills (Habilidades)** do assistente de IA. `.agents/` permanece como fonte canônica; `AGENTS.md` traduz essas regras para o Codex. |
| **Camada 4** | `Arquivo/` | Arquivo e Apoio | Biblioteca de apoio e histórico. Guarda notas filhas (`papel/filha`), MOCs (`papel/moc`), referências passivas e itens concluídos/desativados. |
| **Outros** | `Templates/` | Modelos | Modelos estruturados de notas (como o de notas diárias). |
| **Outros** | `index.md` | Índice Geral | Dashboard central do cofre na raiz do projeto, atualizado automaticamente. |

Regra de higiene: a raiz do cofre deve conter apenas arquivos de navegacao/configuracao. PDFs, imagens e documentos soltos devem ficar em `Arquivo/attachments/`; scripts auxiliares devem ficar em `.agents/scripts/`.

---

## 🏷️ Padrões de Metadados (Obsidian Properties)

Todas as notas criadas na Wiki Ativa ou no Arquivo utilizam o padrão moderno de propriedades do Obsidian. Isso ajuda você a filtrar suas notas e permite que o assistente de IA leia e atualize o cofre programaticamente.

Exemplo de cabeçalho YAML em uma nota:
```yaml
---
created: 2026-06-13
type: projeto # projeto, produto, estudo, ideia, fonte, diario
status: planejado # planejado, em-andamento, em-manutenção, concluído, descontinuado, pendente, arquivado
tags:
  - status/planejado
  - papel/raiz # papel/raiz, papel/filha, papel/moc ou papel/fonte
links:
  - "[[NotaRelacionada]]"
---
```

O template define apenas metadados estruturais. Tags de conteudo, areas, dominios e categorias pertencem ao ambiente de uso. Se uma instalacao precisar de taxonomia propria, declare-a em um arquivo local ignorado pelo Git, como `.agents/assistant/local.md`.

### Tipos de Item (`type`):
*   `projeto`: Iniciativa finita, com prazo e entrega definidos (ex: [[Projeto de Exemplo]]).
*   `produto`: Demandas contínuas que evoluem sem um prazo final rígido (ex: [[Produto de Exemplo]]).
*   `estudo`: Tópicos de aprendizado contínuo ou áreas de interesse (ex: [[Estudo de Exemplo]]).
*   `ideia`: Conceito capturado e não estruturado.
*   `fonte`: Documento de referência imutável na pasta `Fontes/`.
*   `diario`: Notas diárias em `Diario/Daily/`.

### Papel Operacional (`papel/*`)
*   `papel/raiz`: item principal que fica em `Ativo/` e entra no `index.md`.
*   `papel/filha`: dossiê, sub-hub ou artefato de apoio que fica em `Arquivo/` e é linkado por uma raiz.
*   `papel/moc`: índice temático macro listado no `Temas MOC.md`.
*   `papel/fonte`: referência derivada ou material de origem estruturado.

---

## 🤖 O Assistente de IA: agy

O cofre conta com um sistema de automação assistida por IA dividida em dois papéis (Firewall Cognitivo):
1.  **Antigravity (O Arquiteto):** Agente principal responsável pelo desenvolvimento técnico, depuração e modificação das configurações estruturais na pasta `.agents/`.
2.  **agy (O Operador):** Subagente especializado em tarefas rotineiras do cofre. Ele opera as pastas `Inbox/`, `Ativo/` e `Diario/`, mas não pode editar as regras em `.agents/`.

O Codex usa `AGENTS.md` como ponte de compatibilidade para seguir as mesmas regras, lendo `.agents/assistant/` e `.agents/skills/` como fonte canônica antes de executar rotinas.

### ⚡ Habilidades do Assistente (Skills)
O assistente executa rotinas por meio de habilidades definidas em `.agents/skills/`:
*   `capture-idea`: Captura uma ideia no chat e salva um novo arquivo markdown na pasta `Inbox/`.
*   `create-item`: Cria a estrutura de um novo item raiz (`projeto`, `produto`, `estudo`) em `Ativo/`, ou nota filha em `Arquivo/` quando for dossiê/apoio.
*   `process-inbox`: Higieniza e move notas brutas da `Inbox/` para a wiki (`Ativo/` ou `Arquivo/`), movendo o arquivo original para `Fontes/`.
*   `daily-digest`: Executa a transição diária, carregando tarefas pendentes para o dia seguinte, gerando o novo arquivo diário baseado no template e resumindo anotações da seção de Notas.
*   `lint-vault`: Faz uma auditoria de saúde no cofre buscando links quebrados, tags inválidas ou contradições de status.

### Verificacao de Saude do Cofre
Para validar se o cofre continua navegavel por agentes de IA, rode a partir da raiz:

```bash
python .agents/scripts/lint_vault.py
```

Em alguns ambientes Linux/macOS, use `python3` no lugar de `python`. O script nao altera arquivos; ele apenas reporta erros, alertas e sugestoes para correcao assistida.

---

## 🔄 Fluxo de Trabalho Diário (Como Usar)

Para tirar o máximo proveito do seu Segundo Cérebro, sugerimos o seguinte fluxo:

1.  **Captura Rápida (Inbox)**:
    *   Sempre que tiver uma ideia, pensamento ou clipe de artigo, envie para a pasta `Inbox/` (ou peça para o assistente criá-la com o comando de captura de ideia).
2.  **Processamento periódico (Triagem)**:
    *   Use o assistente para rodar o `process-inbox` nas notas da `Inbox/`. Elas serão formatadas com metadados estruturados e movidas para `Ativo/` ou `Arquivo/`.
3.  **Gestão de Itens Ativos (`Ativo/`)**:
    *   Apenas itens raiz acompanháveis ficam na pasta `Ativo/`.
    *   Dossiês, sub-hubs e artefatos de apoio ficam em `Arquivo/` com `papel/filha`, linkados a partir da nota raiz.
    *   No corpo destas notas, defina os cronogramas, anotações de progresso e tarefas (`- [ ]`).
4.  **Operação Diária (`Diario/`)**:
    *   Use a nota diária (`Diario/Daily/DD-MM-YYYY.md`) para registrar o que fará no dia.
    *   **Regra de Espelhamento**: O assistente espelha automaticamente tarefas (`- [ ]`) no diário **apenas** para projetos e produtos com `status: em-andamento`. Projetos planejados ou em standby não poluem seu diário.
5.  **Ciclo de Fechamento**:
    *   No final do dia ou início do próximo, a rotina `daily-digest` encerra o dia anterior, migra tarefas não concluídas para a nova nota diária e consolida as notas escritas pelo usuário.
6.  **Conclusão e Arquivamento**:
    *   Quando um projeto é concluído ou um produto é descontinuado:
        1. Altere o `status` no frontmatter para `concluído` (ou `descontinuado`).
        2. Mova o arquivo físico de `Ativo/` para `Arquivo/`.
        3. Remova a referência a ele do `index.md` e do `Ativo/backlog.md`.

---

## ⚙️ Configuração no Obsidian

Para usar este cofre no Obsidian:
1. Abra o Obsidian e escolha **"Open folder as vault"** (Abrir pasta como cofre).
2. Selecione a pasta raiz deste repositório.
3. Certifique-se de habilitar a visualização de **Properties** (Propriedades) no Obsidian (Configurações > Editor > Properties in document > Display: Visible ou Source).
4. O arquivo `index.md` serve como a página inicial (Home/Dashboard). Você pode usar o plugin *Homepage* do Obsidian para abri-lo automaticamente ao iniciar.

