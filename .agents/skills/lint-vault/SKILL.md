---
name: lint-vault
description: Realiza a auditoria periódica de saúde, consistência e integridade do cofre (detectando contradições, notas órfãs, links perdidos ou conceitos não resolvidos).
---

# Habilidade: Auditoria do Cofre (Lint Vault)

Esta habilidade orienta o subagente agy a escanear a base de conhecimento do cofre para propor melhorias de coesão, consertar links quebrados e detectar dados conflitantes ou obsoletos.

## Diretrizes de Execução

Quando o usuário solicitar um lint, auditoria ou verificação de saúde do cofre (ex: *"Faça o lint do cofre"*):

1. **Varredura Completa:** Analise o catálogo de notas existentes em `Ativo/`, `Diario/Daily/` e `Ativo/backlog.md`.
2. **Critérios de Diagnóstico:**
   *   **Notas Órfãs:** Identifique notas em `Ativo/` que não possuam nenhum link de entrada `[[Nome da Nota]]` vindo de outros arquivos (incluindo o `index.md` e o `backlog.md`).
   *   **Contradições e Obsolescência:** Compare notas de tópicos correlacionados (como itens ativos e diários recentes) para apontar se há informações desatualizadas (ex: um status marcado como "em-andamento" no index mas "concluido" no diário).
   *   **Links Perdidos:** Encontre ocorrências de texto puro que coincidam com títulos de outras notas existentes e sugira convertê-los em links bidirecionais `[[Nota]]`.
   *   **Notas Sementes Ausentes:** Detecte menções frequentes a conceitos que ainda não possuem arquivo `.md` correspondente e sugira sua criação.
3. **Apresentação de Relatório:** Exiba um relatório estruturado no chat contendo:
   *   `Alertas de Consistencia` (Contradições e desatualizações).
   *   `Notas Orfas Encontradas`.
   *   `Sugestoes de Links Cruzados` (Onde adicionar links bidirecionais).
   *   `Sugestoes de Novas Notas Sementes` (Tópicos recorrentes não mapeados).
4. **Proposta de Ação:** Pergunte se o usuário deseja que você corrija os itens listados automaticamente.
5. **Log (Silencioso):** Registre a verificação no .agents/assistant/logs.md (ex: `## [AAAA-MM-DD] lint | Realizada auditoria de saúde do cofre. Detecções: X órfãs, Y links perdidos`).
