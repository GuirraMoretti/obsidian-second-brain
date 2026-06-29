---
name: dump-material
description: Habilidade que gerencia a ingestão, categorização e arquivamento de novos materiais de referência (PDFs, links web, etc.) usando o conceito de MOC e indexação no Temas MOC.md.
---

# Habilidade: Capturar e Arquivar Materiais (dump-material)

Esta habilidade orienta o assistente a receber um material externo (PDF, link web, anotação), analisar seu conteúdo usando um subagente especializado (`theme-associator`), associá-lo a um tema/MOC existente ou criar um novo MOC de referência fria na pasta `Arquivo/`, e manter o `Temas MOC.md` atualizado.

## Diretrizes de Execução

Quando acionada explicitamente pelo usuário (ex: *"/dump-material [Entrada]"*), onde a entrada pode ser uma URL de DOI, uma URL direta de PDF, ou um arquivo PDF local na `Inbox/`:

1. **Processamento da Entrada (download_helper.py):**
   - Execute o script Python `download_helper.py` passando o argumento fornecido pelo usuário.
   - O script analisará a entrada e retornará um JSON contendo o status e os metadados do material.
   - Se o script retornar um erro (`"status": "error"`), informe ao usuário o motivo da falha e interrompa o processo.
   - Se o retorno for sucesso:
     - **Caso de Download Realizado (`"downloaded": true`):** O arquivo PDF foi baixado ou movido para `Fontes/` e seu caminho está listado no campo `filepath`.
     - **Caso de Paywall (`"downloaded": false`):** O PDF não pôde ser obtido legalmente (artigo fechado), mas o script retornou os metadados e a URL do DOI no campo `doi_url`.

2. **Categorização Inteligente via Subagente (`theme-associator`):**
   - O assistente principal invoca o subagente especializado `theme-associator`.
   - O subagente lê o arquivo `Temas MOC.md` na raiz do cofre para conhecer todos os MOCs existentes.
   - O subagente compara o título e metadados obtidos no passo anterior com os temas do `Temas MOC.md`.
   - O subagente retorna um diagnóstico indicando se o material pertence a um tema existente (ex: `Product Operations`) ou se deve ser criado um novo tema (ex: `Rust Programming`) com uma descrição.

3. **Gravação e Associação no MOC:**

   ### Caso A: O Tema Já Existe (MOC Existente)
   1. Abra a nota MOC existente em `Ativo/` ou `Arquivo/` (ex: `Arquivo/Product Operations - MOC.md`).
   2. Insira a referência do material na seção `## Conceitos e Referencias`:
      - **Se o PDF foi baixado:** Insira o link local com o título formatado (ex: `- [[Fontes/nome_do_pdf.pdf|Título do Artigo]]`).
      - **Se for Paywalled:** Insira o link web com metadados (ex: `- [Título do Artigo (Sem PDF)](doi_url) — Autores, Ano.`).
   3. Adicione uma linha no `## Diário de Bordo` da nota registrando a data e o material catalogado.

   ### Caso B: O Tema é Novo (Criação de MOC)
   1. Crie um novo arquivo MOC em `Arquivo/[Nome do Tema] - MOC.md` (deve ser criado em `Arquivo/` como uma referência fria/passiva).
   2. Adicione o cabeçalho YAML frontmatter padrão do cofre:
      ```yaml
      ---
      created: AAAA-MM-DD
      type: estudo
      status: arquivado
      tags:
        - status/arquivado
        - area/pessoal # ou area/evo se o contexto for de trabalho/TCC
        - tema/[tag-do-tema-higienizada]
      links:
        - "[[Fontes/nome_do_arquivo.pdf]]" # se aplicável
      ---
      ```
   3. Estruture o corpo do novo MOC com o seguinte template padrão:
      ```markdown
      # [Nome do Tema] MOC

      ## Objetivo e Impacto
      [Breve descrição sobre o tema]

      ## Motivação e Origem
      Iniciado em [[DD-MM-YYYY]] via dump de material de referência.

      ## Escopo e Contexto
      Armazenar referências conceituais e artigos sobre [Nome do Tema].

      ## Conceitos e Referencias
      - [[Fontes/nome_do_arquivo.pdf|Nome do Artigo]] (ou link/anotação se aplicável)

      ## Diário de Bordo
      ### AAAA-MM-DD
      - MOC criado e primeiro material adicionado.
      ```
   4. Abra o arquivo `Temas MOC.md` na raiz do cofre. Adicione o novo tema na seção `## ❄️ Temas Arquivados (Cold References)` mantendo a ordem alfabética ou inserindo no final da lista:
      `- [[Arquivo/[Nome do Tema] - MOC]] — [Breve descrição do tema].`

4. **Registro de Rastreamento (Diário e Logs):**
   - Localize ou crie o diário do dia atual em `Diario/Daily/DD-MM-YYYY.md`. Na seção `# Notas`, adicione a linha:
     `- **Material Catalogado**: Adicionado o material [Nome do Material] ao tema [[Nome do Tema] - MOC].`
   - Registre o evento silenciosamente no arquivo `.agents/assistant/logs.md` no formato:
     `## [AAAA-MM-DD] dump-material | Material '[Nome do Material]' indexado no tema '[Nome do Tema] MOC'`
