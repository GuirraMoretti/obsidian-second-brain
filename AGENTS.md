# Codex Workspace Instructions

Este arquivo traduz a configuracao historica do Antigravity para o Codex. Ele nao substitui a fonte canonica do cofre: sempre que precisar de detalhe operacional, leia os arquivos em `.agents/assistant/` e as skills em `.agents/skills/`.

## Fontes Canonicas

Leia nesta ordem quando a tarefa envolver o cofre:

1. `index.md` para entender o estado geral dos itens ativos.
2. `.agents/assistant/agy.md` para regras operacionais do Segundo Cerebro.
3. `.agents/assistant/architecture.md` quando a tarefa envolver arquitetura, skills ou comportamento de agentes.
4. `.agents/assistant/decisions.md` antes de mudar convencoes, estrutura ou regras.
5. A skill especifica em `.agents/skills/<nome>/SKILL.md` quando o pedido corresponder a uma rotina existente.

## Protocolo de Recuperacao de Contexto

Para responder perguntas sobre o conteudo do cofre, o agente deve seguir este caminho antes de concluir que nao ha contexto suficiente:

1. Leia `index.md` para identificar itens raiz (`papel/raiz`), status e descricoes de uma linha.
2. Busque termos relevantes com `rg` em `Ativo/`, `Arquivo/`, `Diario/Daily/` e `Temas MOC.md`.
3. Abra a nota ativa, hub ou MOC mais relevante encontrado.
4. Siga os wikilinks diretamente relacionados ao pedido, limitando a leitura ao menor conjunto suficiente.
5. Ao responder, mencione os arquivos consultados quando isso ajudar a rastreabilidade.

Se `index.md` estiver incompleto, desatualizado ou contraditorio com `Ativo/`, trate isso como problema de saude do cofre e rode/planeje `lint-vault` antes de depender do indice.

## Traducao de Papeis

- **Codex como Operador (`agy`)**: use este modo para tarefas rotineiras do cofre, como capturar ideias, processar Inbox, criar itens, atualizar notas, organizar MOCs, migrar diario e auditar consistencia. Siga `agy.md` e a skill correspondente.
- **Codex como Arquiteto**: use este modo apenas quando o usuario pedir mudancas em regras, skills, arquitetura, convencoes ou configuracao do assistente. Leia `architecture.md` e `decisions.md` antes de agir, mantenha a mudanca pequena e registre o resultado em `decisions.md` e `logs.md`.
- **Antigravity** continua sendo a origem historica das convencoes. **Codex funciona como operador/arquiteto compativel** lendo este `AGENTS.md` e as fontes canonicas em `.agents/`, sem depender do runtime do Antigravity.

## Regras de Escrita

- Sempre leia do disco antes de tomar decisao baseada em uma nota ou antes de editar arquivo existente.
- Nao altere `Fontes/` exceto quando uma skill mandar arquivar um original ali. Depois de arquivado, o material em `Fontes/` e imutavel.
- Nao edite `.agents/` durante operacoes rotineiras do cofre. Edite `.agents/` apenas como Arquiteto e com pedido explicito ou necessidade direta da tarefa.
- Nao marque tarefas como concluidas nem promova status para `em-andamento` sem sinal claro do usuario.
- Nao crie tarefas no diario para ideias futuras, sondagens, standby ou registros passivos.
- Preserve Markdown, YAML frontmatter e wikilinks do Obsidian.

## Modelo do Cofre

- `Inbox/`: buffer temporario para capturas e rascunhos.
- `Fontes/`: materiais originais e imutaveis.
- `Ativo/`: painel executivo de itens raiz acompanhaveis (`papel/raiz`), como projetos, produtos e estudos principais.
- `Diario/Daily/`: notas diarias no formato `DD-MM-YYYY.md`.
- `.agents/`: regras, historico e skills do assistente.
- `Arquivo/`: notas filhas, dossies de apoio, MOCs, referencias passivas e itens encerrados.
- `Temas MOC.md`: indice central de MOCs tematicos.

## Metadados Padrao

Notas novas devem usar Obsidian Properties:

```yaml
---
created: AAAA-MM-DD
type: projeto
status: planejado
description: "Resumo curto de uma linha."
tags:
  - status/planejado
  - area/pessoal
  - papel/raiz
links: []
---
```

Tipos validos: `projeto`, `produto`, `estudo`, `ideia`, `fonte`, `diario`.
Status validos: `planejado`, `em-andamento`, `em-manutenção`, `concluído`, `descontinuado`, `pendente`, `arquivado`.
Papeis validos em tags: `papel/raiz`, `papel/filha`, `papel/moc`, `papel/fonte`.

Para definicoes completas, consulte `.agents/assistant/glossary.md`.

## Skills Locais

Use as skills locais quando o pedido bater com uma delas. Antes de executar, leia o `SKILL.md` correspondente.

- `capture-idea`: salvar ideias rapidas em `Inbox/`.
- `create-item`: criar projeto, produto ou estudo em `Ativo/`.
- `process-inbox`: triagem de notas brutas da `Inbox/`.
- `daily-digest`: fechamento/abertura diaria e migracao de pendencias.
- `dump-material`: ingestao de PDFs, links e referencias em MOCs.
- `lint-vault`: auditoria de saude do cofre.
- `vault-sync`: sincronizacao com GitHub.

Quando uma skill do Antigravity mencionar subagentes, adapte para os recursos disponiveis no Codex, mantendo o mesmo contrato: ler as instrucoes referenciadas, operar no menor escopo possivel e registrar mudancas relevantes.

## Mapa Rapido de Intencao

- "Anota", "registra", "guarda isso": registre uma nota breve, normalmente no diario ou via `capture-idea`, sem criar tarefa automaticamente.
- "Preciso fazer", "tenho que": crie checkbox apenas se for acao concreta.
- "Cria um projeto/produto/estudo": use `create-item` e marque como `papel/raiz`, salvo se o usuario disser que e dossie/apoio de outro item.
- "Apenas para o futuro", "sondagem", "standby": trate como registro passivo, nao como demanda ativa.
- "Catalogar PDF/artigo/link": use `dump-material`.
- "Fechar o dia", "abrir o dia", "digest": use `daily-digest`.

## Registro de Mudancas

Ao mudar arquitetura, convencoes, skills ou arquivos de configuracao do assistente:

1. Atualize `.agents/assistant/decisions.md` com a decisao e o alinhamento de metas.
2. Adicione uma linha em `.agents/assistant/logs.md`.
3. Se a mudanca afetar uso humano do cofre, atualize tambem `README.md`.
