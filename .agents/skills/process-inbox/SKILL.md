---
name: process-inbox
description: Processa, formata e organiza arquivos markdown brutos da pasta Inbox/ para a estrutura da wiki permanente (Ativo/ ou Arquivo/), arquivando a nota original em Fontes/.
---

# Habilidade: Organizar e Processar Inbox

Esta habilidade orienta o subagente agy a realizar a triagem, enriquecimento e arquivamento das notas brutas depositadas na pasta Inbox/.

## Diretrizes de Execução

Quando solicitado a organizar ou processar a inbox:

1. **Leitura:** Varra e leia todos os arquivos `.md` na pasta Inbox/ (ignorar arquivos do sistema como `.gitkeep`).
2. **Varredura do Cofre:** Mapeie os arquivos existentes em `Ativo/` para propor links bidirecionais (`[[Nome da Nota]]`) altamente relevantes no texto da nota de entrada.
3. **Classificação de Destino:** Classifique cada nota para o diretório correto, usando o campo `type` para definir a natureza do conteúdo:
   *   `Ativo/` (type: `estudo`) — Assuntos de interesse contínuo, aprendizado técnico e conceitos de longo prazo.
   *   `Ativo/` (type: `projeto`) — Iniciativas com cronogramas, metas específicas e checklists.
   *   `Ativo/` (type: `produto`) — Ferramentas, sistemas ou artefatos mantidos continuamente.
   *   `Arquivo/` — Notas arquivadas, referências antigas ou inativas.
4. **Renomeação Descritiva:** Recomende um nome de arquivo limpo, higienizado e descritivo (sem caracteres especiais ou timestamps de data no nome do arquivo).
5. **Estrutura de Metadados (Obsidian Properties):** Crie ou atualize o cabeçalho YAML frontmatter da nota com a seguinte estrutura de propriedades moderna:
   ```yaml
   ---
   created: AAAA-MM-DD
   type: tipo-da-nota # estudo, projeto, produto, ideia, fonte, diario
   status: estado-atual # planejado, em-andamento, em-manutenção, concluído, descontinuado, pendente, arquivado
   tags:
     - tag1
     - area/evo # ou area/pessoal
   links:
     - "[[NotaRelacionada]]"
   ---
   ```
6. **Escrever nota no Destino:** Salve a nota estruturada com as propriedades e links bidirecionais no diretório de destino correspondente.
7. **Arquivamento da Fonte:** Mova a nota original bruta de `Inbox/` para Fontes/. **NÃO delete a nota original.**
8. **Atualizações de Índices (Silenciosas):**
   *   Se for um item ativo (estudo, projeto ou produto), adicione na seção `Ativo` do index.md.
   *   Adicione um registro no .agents/assistant/logs.md descrevendo as notas processadas e destinos.
