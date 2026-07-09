---
name: process-inbox
description: Processa, formata e organiza arquivos markdown brutos da pasta Inbox/ para a estrutura da wiki permanente (Ativo/ ou Arquivo/), arquivando a nota original em Fontes/.
---

# Habilidade: Organizar e Processar Inbox

Esta habilidade orienta o subagente agy a realizar a triagem, enriquecimento e arquivamento das notas brutas depositadas na pasta Inbox/.

## Diretrizes de Execução

Quando solicitado a organizar ou processar a inbox:

1. **Leitura:** Varra e leia todos os arquivos `.md` na pasta Inbox/ (ignorar arquivos do sistema como `.gitkeep`).
2. **Varredura do Cofre:** Mapeie os arquivos existentes em `Ativo/`, `Arquivo/` e `Temas MOC.md` para propor links bidirecionais (`[[Nome da Nota]]`) altamente relevantes no texto da nota de entrada.
3. **Classificação de Destino:** Classifique cada nota usando `type` para a natureza do conteúdo e `papel/*` para a função operacional:
   *   `Ativo/` + `papel/raiz` — projeto, produto ou estudo principal que deve aparecer no painel de decisão.
   *   `Arquivo/` + `papel/filha` — dossiê, sub-hub, artefato de apoio ou nota viva subordinada a uma raiz.
   *   `Arquivo/` + `papel/moc` — índice temático macro.
   *   `Arquivo/` + `papel/filha` ou `papel/fonte` — referências antigas, passivas ou materiais estruturados.
4. **Renomeação Descritiva:** Recomende um nome de arquivo limpo, higienizado e descritivo (sem caracteres especiais ou timestamps de data no nome do arquivo).
5. **Estrutura de Metadados (Obsidian Properties):** Crie ou atualize o cabeçalho YAML frontmatter da nota com a seguinte estrutura de propriedades moderna:
   ```yaml
   ---
   created: AAAA-MM-DD
   type: tipo-da-nota # estudo, projeto, produto, ideia, fonte, diario
   status: estado-atual # planejado, em-andamento, em-manutenção, concluído, descontinuado, pendente, arquivado
   description: "Resumo de uma linha da nota"
   tags:
     - status/estado-atual
     - papel/raiz # ou papel/filha, papel/moc, papel/fonte
     # tags locais opcionais pertencem ao ambiente de uso
   links:
     - "[[NotaRelacionada]]"
   ---
   ```
6. **Escrever nota no Destino:** Salve a nota estruturada com as propriedades e links bidirecionais no diretório de destino correspondente.
7. **Arquivamento da Fonte:** Mova a nota original bruta de `Inbox/` para Fontes/. **NÃO delete a nota original.**
8. **Atualizações de Índices (Silenciosas):**
   *   Se for `papel/raiz`, adicione na seção `Ativo` do index.md.
   *   Se for `papel/filha`, não adicione no index.md; atualize ou sugira atualizar a nota raiz com um wikilink para a nova nota.
   *   Adicione um registro no .agents/assistant/logs.md descrevendo as notas processadas e destinos.
