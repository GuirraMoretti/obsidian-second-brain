# 🧠 Segundo Cérebro — Template de Wiki Pessoal com IA (Obsidian + Antigravity)

Um sistema completo de **base de conhecimento pessoal** (Second Brain / Personal Knowledge Management) que utiliza o **Obsidian** como editor e o assistente de IA **Antigravity / Codex** como copiloto inteligente para organizar, curar e manter suas notas, projetos e estudos.

> **O que torna este projeto diferente?** Este não é apenas um template de notas — é um **sistema operacional de produtividade** com habilidades de IA que automatizam a captura de ideias, organização de inbox, gestão de projetos, auditoria de consistência, indexação de referências e sincronização com GitHub.

---

## ✨ Features

- 📥 **Captura Rápida de Ideias** — Salve pensamentos no chat e eles viram notas estruturadas na Inbox automaticamente.
- 📋 **Processamento Inteligente** — Notas brutas na Inbox são higienizadas, enriquecidas com metadados estruturados e movidas para a Wiki permanente.
- 📅 **Digest Diário Automatizado** — Transição diária com migração de tarefas pendentes, criação da nota do novo dia e consolidação das notas escritas.
- 📁 **Criação Estruturada de Itens** — Criação de projetos, produtos e estudos com templates adaptativos por tipo, status e domínio.
- 📚 **Ingestão de Referências** — Ingestão inteligente de PDFs e artigos direto para a pasta de fontes com categorização automática em MOCs (Maps of Content).
- 🔍 **Linter de Saúde Portátil** — Script Python portátil (`lint_vault.py`) para auditar links quebrados, órfãs, inconsistências de status e higiene do cofre.
- 🔄 **Sincronização com GitHub** — Processo robusto de Push/Pull Git com resolução automática de conflitos para uso multi-dispositivo.

---

## 🚀 Setup Rápido

### Pré-requisitos
- [Obsidian](https://obsidian.md/) instalado.
- [Antigravity](https://antigravity.google/) configurado (IDE com suporte a agentes de IA) ou outro assistente compatível com o protocolo Codex.

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SEU-USUARIO/obsidian-second-brain.git
   ```

2. **Abra no Obsidian:**
   - Abra o Obsidian → "Open folder as vault" → selecione a pasta clonada.
   - Habilite a visualização de **Properties** (Configurações > Editor > Properties in document > Display: Visible).

3. **Configure seu assistente de IA:**
   - Abra o projeto clonado em seu assistente habilitado com Antigravity/Codex.
   - O assistente lerá as regras do [AGENTS.md](AGENTS.md) e as habilidades locais na pasta `.agents/` automaticamente.

4. **Personalize:**
   - Edite o `index.md` e o `Temas MOC.md` para adicionar seus projetos, áreas de foco e estudos iniciais.

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

> [!IMPORTANT]
> **Regra de Higiene da Raiz:** A raiz do cofre deve conter apenas arquivos de navegação/configuração. Anexos, PDFs, imagens e documentos soltos de apoio devem ficar em `Arquivo/attachments/` (ou em `Fontes/` se forem materiais originais); scripts auxiliares devem ficar em `.agents/scripts/`.

---

## 🏷️ Padrões de Metadados (Obsidian Properties)

Todas as notas criadas na Wiki Ativa ou no Arquivo utilizam o padrão moderno de propriedades do Obsidian (YAML frontmatter). Isso ajuda você a filtrar suas notas e permite que o assistente de IA leia e atualize o cofre programaticamente.

Exemplo de cabeçalho YAML em uma nota:
```yaml
---
created: 2026-06-13
type: projeto # projeto, produto, estudo, ideia, fonte, diario
status: planejado # planejado, em-andamento, em-manutenção, concluído, descontinuado, pendente, arquivado
tags:
  - status/planejado
  - area/pessoal # area/pessoal (Pessoal) ou area/trabalho (Trabalho)
  - papel/raiz # papel/raiz, papel/filha, papel/moc ou papel/fonte
links:
  - "[[NotaRelacionada]]"
---
```

### Tipos de Item (`type`):
*   `projeto`: Iniciativa finita, com prazo e entrega definidos (ex: *Lançamento de Campanha*).
*   `produto`: Demandas contínuas que evoluem sem um prazo final rígido (ex: *Dashboard Financeiro*).
*   `estudo`: Tópicos de aprendizado contínuo ou áreas de interesse (ex: *Curso de Machine Learning*).
*   `ideia`: Conceito capturado e não estruturado.
*   `fonte`: Documento de referência imutável na pasta `Fontes/`.
*   `diario`: Notas diárias em `Diario/Daily/`.

### Papel Operacional (`papel/*`):
*   `papel/raiz`: Item principal que fica em `Ativo/` e entra obrigatoriamente no `index.md`.
*   `papel/filha`: Dossiê, sub-hub ou nota de apoio subordinada a uma nota raiz. Fica guardado em `Arquivo/` para manter a pasta `Ativo/` limpa.
*   `papel/moc`: Índice temático macro (Map of Content) listado no `Temas MOC.md`.
*   `papel/fonte`: Referência derivada ou material de origem estruturado.

---

## 🤖 O Assistente de IA: agy

O cofre conta com um sistema de automação assistida por IA dividida em dois papéis (**Firewall Cognitivo**):
1.  **Antigravity (O Arquiteto):** Agente principal responsável pelo desenvolvimento técnico, depuração e modificação das configurações estruturais na pasta `.agents/`.
2.  **agy (O Operador):** Subagente especializado em tarefas rotineiras do cofre. Ele opera as pastas `Inbox/`, `Ativo/` e `Diario/`, mas não pode editar as regras em `.agents/`.

O Codex usa o arquivo [AGENTS.md](AGENTS.md) como ponte de compatibilidade para seguir as mesmas regras, lendo `.agents/assistant/` e `.agents/skills/` como fonte canônica.

### ⚡ Habilidades do Assistente (Skills)
O assistente executa rotinas por meio de habilidades definidas em `.agents/skills/`:
*   `capture-idea`: Captura uma ideia no chat e salva um novo arquivo markdown na pasta `Inbox/`.
*   `create-item`: Cria a estrutura de um novo item raiz (`projeto`, `produto`, `estudo`) em `Ativo/`, ou nota filha em `Arquivo/` quando for dossiê/apoio.
*   `process-inbox`: Higieniza e move notas brutas da `Inbox/` para a wiki (`Ativo/` ou `Arquivo/`), movendo o arquivo original para `Fontes/`.
*   `daily-digest`: Executa a transição diária, carregando tarefas pendentes para o dia seguinte, gerando o novo arquivo diário baseado no template e resumindo anotações da seção de Notas.
*   `dump-material`: Ingere PDFs e referências web na pasta `Fontes/` e indexa-os no MOC temático correspondente.
*   `lint-vault`: Faz uma auditoria de saúde no cofre buscando links quebrados, tags inválidas ou contradições de status.
*   `vault-sync`: Executa sincronização de segurança via Git (push/pull) com o repositório remoto, resolvendo conflitos de forma autônoma.

### 🔍 Verificação de Saúde do Cofre

Para validar se o cofre continua navegável por agentes de IA e sem links perdidos ou propriedades quebradas, rode a partir da raiz:

```bash
python .agents/scripts/lint_vault.py
```

O script em Python puro (sem dependências externas) roda em Windows, Linux e macOS. Ele não altera seus arquivos; ele apenas reporta erros, alertas e sugestões de links cruzados para correção assistida.

---

## 🔄 Fluxo de Trabalho Diário (Como Usar)

Para tirar o máximo proveito do seu Segundo Cérebro, sugerimos o seguinte fluxo:

1.  **Captura Rápida (Inbox)**:
    *   Sempre que tiver uma ideia, pensamento ou link de artigo, envie para a pasta `Inbox/` (ou peça para o assistente criá-la com a skill `capture-idea`).
2.  **Processamento periódico (Triagem)**:
    *   Use o assistente para rodar a skill `process-inbox` nas notas da `Inbox/`. Elas serão formatadas com metadados estruturados e movidas para `Ativo/` ou `Arquivo/`.
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
3. Certifique-se de habilitar a visualização de **Properties** no Obsidian (Configurações > Editor > Properties in document > Display: Visible ou Source).
4. O arquivo `index.md` serve como a página inicial (Home/Dashboard). Você pode usar o plugin *Homepage* do Obsidian para abri-lo automaticamente ao iniciar.

---

## 📄 Licença

Este projeto está licensed sob a [MIT License](LICENSE).

---

## 🙏 Contribuições

Contribuições são super bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias nas skills, novos templates de notas ou correções nos scripts auxiliares.
