---
name: daily-digest
description: Consolida o fechamento e a abertura de dias no cofre. Migra tarefas pendentes do diário anterior e invoca o subagente notes-consolidator para extrair e organizar conhecimentos inseridos na seção de Notas.
---

# Habilidade: Consolidacao e Abertura Diaria (daily-digest)

Esta habilidade orienta o assistente a gerenciar o encerramento das anotações do dia anterior/atual e organizar a transição de tarefas, conhecimentos e o monitoramento de itens ativos para o novo dia.

## Diretrizes de Execução

Quando solicitado a fazer o daily-digest, consolidar o dia ou gerenciar o fluxo diário:

1. **Obtenção da Data:** Determine a data atual no formato `DD-MM-YYYY` (doravante referida como `{data-de-hoje}`, ex: `11-06-2026`).
2. **Identificação do Modo:** Verifique a existência de `Diario/Daily/{data-de-hoje}.md` no disco.
   *   **Modo Encerramento (`Diario/Daily/{data-de-hoje}.md` já existe):**
       *   O objetivo é processar o dia de hoje que está terminando.
       *   **Consolidação de Notas:** Invoque o subagente `notes-consolidator` com a instrução: *"Analise a seção de notas do arquivo Diario/Daily/{data-de-hoje}.md, extraia conhecimentos, ideias ou itens relevantes e crie ou atualize os arquivos correspondentes em Ativo/, Arquivo/ ou Inbox/ seguindo as regras de Obsidian Properties (incluindo `description` e `papel/*` no frontmatter) e aplicando a Classificação Inteligente para itens existentes. Use Ativo/ apenas para `papel/raiz`; use Arquivo/ para `papel/filha`, MOCs e referências. Explique suas decisões de arquivamento."*
       *   **Inspeção de Itens Ativos e Prazos:** Invoque o subagente `project-tracker` com a instrução: *"Analise os arquivos na pasta Ativo/ com `papel/raiz` e type: projeto ou type: produto. Gere um 'Resumo de Impedimentos' para gargalos ativos e uma lista de 'Eventos Futuros e Prazos', extraindo apenas as tarefas pendentes com datas futuras explícitas dos cronogramas."*
            > **Nota:** Use os prompts documentados em [references/subagents.md](references/subagents.md) para instanciar os subagentes via `define_subagent`.
       *   **Rollup de Tarefas e Lembretes:**
            1. Faça uma leitura fresca do arquivo `Diario/Daily/{data-de-hoje}.md` diretamente do disco físico.
            2. Extraia as tarefas que comecem com `- [ ]` (não marcadas) de qualquer checklist para migração.
            3. Leia a seção `# Eventos Futuros e Prazos` do diário de hoje. Identifique lembretes/prazos avulsos (itens com data `DD/MM/AAAA` que não referenciam projetos/produtos ativos em `Ativo/`):
               - Os que tiverem data igual a `{data-de-amanha}` devem ser convertidos em tarefas ativas `- [ ] [Descrição]` na seção apropriada do template diário local.
               - Os que tiverem data posterior a `{data-de-amanha}` devem ser preservados como eventos futuros no novo diário.
       *   **Criação do Dia Seguinte:** Calcule a data do dia seguinte no formato `DD-MM-YYYY` (doravante referida como `{data-de-amanha}`, ex: `12-06-2026`). Gere o arquivo `Diario/Daily/{data-de-amanha}.md` baseado no template `Templates/Notas Diarias.md`. Preencha a seção `# Eventos Futuros e Prazos` mesclando ordenadamente os eventos gerados pelo `project-tracker` com os eventos futuros preservados. Insira as tarefas migradas nas seções existentes mais adequadas do template local, mantendo os cabeçalhos de projeto se aplicável. Se a seção correta não estiver clara, use `# Notas` ou pergunte ao usuário. Se houver um Resumo de Impedimentos, anexe-o no final do arquivo.
   *   **Modo Planejamento (`Diario/Daily/{data-de-hoje}.md` não existe):**
       *   O objetivo é iniciar o dia atual importando as pendências do dia anterior.
       *   **Localização de Ontem:** Encontre o diário mais recente existente anterior a hoje na pasta `Diario/Daily/` (doravante referido como `Diario/Daily/{data-de-ontem}.md`, ex: `10-06-2026.md`).
       *   **Consolidação de Ontem:** Invoque o subagente `notes-consolidator` com a instrução: *"Analise a seção de notas do arquivo Diario/Daily/{data-de-ontem}.md, extraia conhecimentos, ideias ou itens relevantes e crie ou atualize os arquivos correspondentes em Ativo/, Arquivo/ ou Inbox/ seguindo as regras de Obsidian Properties (incluindo `description` e `papel/*` no frontmatter) e aplicando a Classificação Inteligente para itens existentes. Use Ativo/ apenas para `papel/raiz`; use Arquivo/ para `papel/filha`, MOCs e referências. Explique suas decisões de arquivamento."*
       *   **Inspeção de Itens Ativos e Prazos:** Invoque o subagente `project-tracker` com a instrução: *"Analise os arquivos na pasta Ativo/ com `papel/raiz` e type: projeto ou type: produto. Gere um 'Resumo de Impedimentos' para gargalos ativos e uma lista de 'Eventos Futuros e Prazos', extraindo apenas as tarefas pendentes com datas futuras explícitas dos cronogramas."*
            > **Nota:** Use os prompts documentados em [references/subagents.md](references/subagents.md) para instanciar os subagentes via `define_subagent`.
       *   **Rollup de Tarefas e Lembretes:**
            1. Faça uma leitura fresca do arquivo `Diario/Daily/{data-de-ontem}.md` diretamente do disco físico.
            2. Extraia as tarefas que comecem com `- [ ]` (não marcadas) de qualquer checklist para migração.
            3. Leia a seção `# Eventos Futuros e Prazos` do diário de ontem. Identifique lembretes/prazos avulsos (itens com data `DD/MM/AAAA` que não referenciam projetos/produtos ativos em `Ativo/`):
               - Os que tiverem data igual a `{data-de-hoje}` devem ser convertidos em tarefas ativas `- [ ] [Descrição]` na seção apropriada do template diário local.
               - Os que tiverem data posterior a `{data-de-hoje}` devem ser preservados como eventos futuros no novo diário.
       *   **Abertura de Hoje:** Crie a nota diária `Diario/Daily/{data-de-hoje}.md` baseada no template. Preencha a seção `# Eventos Futuros e Prazos` mesclando ordenadamente os prazos do `project-tracker` com os eventos futuros preservados. Insira as tarefas migradas nas seções existentes mais adequadas do template local, mantendo os cabeçalhos de projeto se aplicável. Se a seção correta não estiver clara, use `# Notas` ou pergunte ao usuário. Se houver um Resumo de Impedimentos, anexe-o no final do arquivo (sob um cabeçalho `# Impedimentos de Projetos`).

3. **Log e Feedback:** 
   - Informe ao usuário o modo executado (Encerramento ou Planejamento).
   - Apresente o resumo das notas consolidadas, das tarefas migradas e, em destaque, se algum item apresentou **impedimentos**.
   - Grave silenciosamente o evento no .agents/assistant/logs.md no formato:
     `## [AAAA-MM-DD] digest | Modo: [Modo] | Migradas X tarefas | Notas consolidadas.`
