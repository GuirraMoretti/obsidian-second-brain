---
name: capture-idea
description: Captura ideias rápidas no chat e as salva como notas na pasta Inbox/ usando o título da ideia como nome do arquivo.
---

# Habilidade: Capturar Ideia Rápida

Esta habilidade orienta o subagente agy a registrar de forma rápida e sem fricção pensamentos soltos, demandas ou insights na Inbox.

## Diretrizes de Execução

Quando o usuário disser algo para capturar ou guardar como ideia (ex: *"Capture a ideia: Titulo"*):

1. **Definição de Título e Conteúdo:** Identifique o título principal da ideia e qualquer descrição fornecida pelo usuário.
2. **Nome de Arquivo Higienizado:** Crie um nome de arquivo a partir do título da ideia (ex: `Meu Estudo de RAG.md`). **NÃO use carimbos de data ou timestamps no nome do arquivo.**
3. **Propriedades (Obsidian Properties):** Adicione as propriedades modernas:
   ```yaml
   ---
   created: AAAA-MM-DD
   type: ideia
   status: pendente
   description: ""
   tags:
     - inbox/ideia-rapida
   links: []
   ---
   ```
4. **Estrutura da Nota:** Escreva o conteúdo com o título principal como cabeçalho H1 e a descrição da ideia logo abaixo.
5. **Gravação:** Salve o arquivo na pasta `Inbox/`.
6. **Registro no Diário:** Localize o diário do dia atual em `Diario/Daily/DD-MM-YYYY.md` (se não existir, crie-o baseado no template). Na seção `# Notas`, adicione a linha:
   `- **Ideia Rápida**: Capturada a ideia de [[Nome da Ideia]].`
7. **Log (Silencioso):** Adicione o registro no `.agents/assistant/logs.md` (ex: `## [AAAA-MM-DD] capture | Capturada a ideia rápida: Titulo da Ideia`).

