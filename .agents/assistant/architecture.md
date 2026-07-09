# Arquitetura e Habilidades do Assistente

Este documento define a arquitetura técnica e as habilidades (skills) operacionais do assistente Antigravity neste workspace. É um arquivo de configuração de comportamento exclusivo do agente.

## Modelo de Camadas da LLM Wiki

A arquitetura do cofre segue a divisão em 5 camadas lógicas (de Camada 0 a Camada 4) detalhadas no manual geral do assistente [agy.md](agy.md). 

As diretrizes operacionais de cada pasta e as regras de preservação de escrita encontram-se centralizadas no [agy.md](agy.md) para garantir uma única fonte de verdade.

## 🤖 Habilidades de Execução (Agent Skills)

As habilidades são carregadas pelo agente a partir dos arquivos localizados no diretório `.agents/skills/`:

*   **[process-inbox](../skills/process-inbox/SKILL.md):** Processamento e organização de rascunhos em Obsidian Properties, arquivando o arquivo bruto original em `Fontes/`.
*   **[daily-digest](../skills/daily-digest/SKILL.md):** Consolidação diária. Executa a migração de tarefas e delega a extração de notas diárias para o subagente especialista `notes-consolidator` para criar tópicos permanentes.
*   **[create-item](../skills/create-item/SKILL.md):** Criação estruturada de novos projetos em `Ativo/` utilizando propriedades modernas.
*   **[capture-idea](../skills/capture-idea/SKILL.md):** Captura rápida de ideias salvando arquivos na Inbox com o título higienizado.
*   **[lint-vault](../skills/lint-vault/SKILL.md):** Auditoria de saude do cofre usando o script portatil `.agents/scripts/lint_vault.py` para detectar notas orfas, divergencias de status, referencias ausentes e lacunas de metadados.
*   **[dump-material](../skills/dump-material/SKILL.md):** Ingestão e categorização automática de referências externas em MOCs correspondentes.
*   **[vault-sync](../skills/vault-sync/SKILL.md):** Sincronização bidirecional do cofre com o repositório remoto no GitHub, incluindo resolução autônoma de conflitos.

## Guia de Referência de Arquivos
*   **Regras Gerais do Cofre:** [agy.md](agy.md)
*   **Histórico de Decisões:** [decisions.md](decisions.md)
*   **Planejamento de Evolução:** [roadmap.md](roadmap.md)
*   **Glossário de Tipos e Status:** [glossary.md](glossary.md)
*   **Documentação da Plataforma Antigravity:** [platform-reference.md](platform-reference.md)

## Firewall Cognitivo e Subagentes
O sistema implementa uma forte separação de papéis para evitar alucinações de alteração de arquitetura:
*   **Arquiteto (Antigravity historico / Codex compativel):** Agente principal responsável por configurar, manter e auditar a arquitetura em `.agents/`. Tem a responsabilidade obrigatória de registrar toda alteração estrutural, refatoração de pastas/nomes ou decisões de design no histórico [decisions.md](decisions.md) e [logs.md](logs.md) antes de concluir qualquer tarefa.
*   **`agy` (Operador Diário):** Subagente restrito (instanciado via `define_subagent`) que NÃO pode editar a arquitetura. Ele é responsável por operar a `Inbox/`, `Diario/`, `Ativo/` e `Arquivo/` (incluindo a gestão, criação e atualização de MOCs temáticos e do `Temas MOC.md`) no dia a dia.
*   **`notes-consolidator`:** Subagente acionado pelo `daily-digest` (via Agy) para curar notas soltas.
*   **`theme-associator`:** Subagente acionado pela skill `dump-material` para analisar materiais semânticos e mapear MOCs correspondentes.

## 📜 Governança de Mudanças (Arquitetura e Decisões)
Para garantir a rastreabilidade e evitar a perda de contexto histórico sobre as decisões do cofre:
1. **Registro Obrigatório de ADRs (Architecture Decision Records):** Qualquer mudança física (renomeação de pastas, convenções de arquivos como `- MOC`, reestruturações) ou lógica (novas habilidades de IA) deve ser acompanhada de uma nova entrada no topo do arquivo [decisions.md](decisions.md) detalhando o *Alinhamento de Metas* e as *Decisões de Design*.
2. **Auditoria de Documentação:** Em todas as sessões de desenvolvimento, o agente principal deve rodar uma verificação de consistência entre o estado atual das pastas/arquivos e o histórico de decisões para certificar-se de que tudo o que foi alterado está devidamente registrado.
