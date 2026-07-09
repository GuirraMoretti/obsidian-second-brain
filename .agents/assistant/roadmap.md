# Roteiro de Implementações Futuras

Este documento planeja evoluções de engenharia e melhorias de arquitetura técnica a serem autodesenvolvidas pelo assistente nas próximas sessões.

---

## Otimizações Planejadas

### 1. Busca Semântica Local via Servidor MCP
*   **Problema:** À medida que a Wiki cresce além de centenas de notas, a leitura de arquivos lineares e busca textual por string (grep) aumenta o consumo de tokens e a latência das buscas da IA.
*   **Solução:** Integrar um servidor MCP local (como o `qmd` ou extensões vetoriais locais como `sqlite-vss`) para habilitar busca semântica híbrida, permitindo que a IA encontre conexões conceituais sutis e cruze informações de forma muito mais precisa.

### 2. Validador de Esquema de Metadados (Properties Linter)
*   **Problema:** Metadados inseridos manualmente ou por scripts antigos podem quebrar convenções e dificultar consultas via Dataview.
*   **Solução:** Criar ou estender a skill `lint-vault` para validar ativamente se todas as notas em `Ativo/` seguem a estrutura de Obsidian Properties (`created`, `type`, `status`, `tags`, `links`) e alertar o usuário sobre campos inválidos ou inexistentes.

### 3. Refinamento de Prompts de Subagentes e Revisão de Papéis
*   **Problema:** O subagente `notes-consolidator` recém-criado possui um prompt básico de estruturação de conhecimento, mas que precisa ser refinado para curar melhor tópicos complexos, definir regras de tags e alinhar o papel de todos os outros agentes de forma coordenada.
*   **Solução:** Conduzir uma sessão colaborativa de engenharia de prompts com o usuário para revisar todos os prompts do assistente e especializar o `notes-consolidator`.

### 4. Integração com Agenda e E-mail via MCP / Skill
*   **Problema:** Necessidade de coordenar tarefas, prazos e notas diárias com eventos externos de calendário e mensagens de e-mail sem precisar sair do ecossistema do assistente.
*   **Solução:** Implementar integração com serviços externos (Google Workspace / Office 365) via Servidor MCP ou por meio de uma Skill local escrita em Python/Node.js, importando automaticamente compromissos para as Notas Diárias (`Diario/`) e e-mails importantes ou acionáveis para a `Inbox/`.

---

## Pendências da Auditoria (Agy)

Melhorias identificadas na auditoria de arquitetura e prompts que foram adiadas para execução posterior:

### Prioridade 1 (Alta)
*   [ ] **Ambiguidade de Nomes no daily-digest (C2):** Mudar placeholders (`Hoje.md`, `Ontem.md`) para caminhos dinâmicos calculados via data explícita (ex: `Diario/Daily/{DD-MM-YYYY}.md`).
*   [ ] **Eliminar Redundâncias de Documentação:** Definir fontes únicas da verdade (*source of truth*) para conceitos repetidos (como as 3 Camadas no `agy.md` e o Firewall no `architecture.md`) e usar links para referenciá-los.
*   [x] **Classificar Inbox/ e Arquivo/:** Definir formalmente as regras de camada para `Inbox/` (Camada 0 - Buffer) e `Arquivo/` (Wiki inativa) nos guias de arquitetura. *(Concluído em 2026-06-12 na reestruturação Ativo/)*
*   [ ] **Sanear index.md:** Corrigir os links internos quebrados no índice central e remover datas e caminhos *hardcoded*.
*   [ ] **Alinhamento do backlog.md:** Corrigir a contradição do status do `backlog.md` (que usa `status: ativo`) com o manual `agy.md` (que prescreve `em-andamento`, `planejado`, etc.).

### Prioridade 2 (Média/Baixa)
*   [ ] **Exemplos e Exceções nas Skills:** Adicionar seções `## Exemplo` (input/output) e `## Tratamento de Exceções` (ex: inbox vazia, arquivo diário inexistente) em cada SKILL.md.
*   [ ] **Padronização de Logs:** Unificar o formato de log de execução gerado pelas skills em `logs.md`.
*   [ ] **Limpeza de Pastas e Termos Fantasmas:** Documentar/remover o diretório `Diario/Daily Materials/` e definir explicitamente ou remover o conceito de "Classificação Inteligente".

---

## Guia de Referência
*   **Arquitetura Técnica:** [architecture.md](architecture.md)
*   **Histórico de Decisões:** [decisions.md](decisions.md)
