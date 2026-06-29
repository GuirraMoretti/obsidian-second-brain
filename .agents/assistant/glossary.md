# Glossário de Tipos e Status

Este documento define formalmente os tipos de itens, status e ciclos de vida utilizados no cofre. É a referência canônica para todas as skills e subagentes.

---

## Tipos de Item (`type`)

| Tipo | Descrição | Quando usar | Ciclo de vida |
|---|---|---|---|
| `projeto` | Iniciativa finita com prazo e entrega definidos | Formatura, viagem, sprint específica | planejado → em-andamento → concluído → Arquivo/ |
| `produto` | Demanda contínua que evolui e recebe melhorias | Dashboard Produto, ferramentas internas | em-andamento → em-manutenção ↔ em-andamento → descontinuado → Arquivo/ |
| `estudo` | Tema de aprendizado, pesquisa ou interesse contínuo | Product Ops, LLM Wiki, tecnologias | em-andamento → concluído → Arquivo/ (atualizável mesmo arquivado) |
| `ideia` | Conceito capturado, sem forma definida ainda | Insights, brainstorms, sugestões | pendente → vira projeto/produto/estudo, ou → Arquivo/ |
| `fonte` | Material de referência original imutável | Artigos, PDFs, notas clipadas | Imutável em Fontes/ |
| `diario` | Nota diária temporal | Registro do dia | Vive em Diario/Daily/ |

---

## Status (`status`)

| Status | Quando usar |
|---|---|
| `planejado` | Item criado mas ainda não priorizado |
| `em-andamento` | Ativamente sendo trabalhado |
| `em-manutenção` | Produto entregue, pode receber melhorias esporádicas |
| `concluído` | Finalizado, pronto para arquivar |
| `descontinuado` | Abandonado ou depreciado |
| `pendente` | Aguardando triagem (ideias na inbox) |
| `arquivado` | Movido para Arquivo/ |

---

## Regras de Transição

### Reativação
Um item em `Arquivo/` com `status: concluído` pode ser reativado:
1. Mover de `Arquivo/` → `Ativo/`
2. Alterar `status` para `em-andamento`
3. Registrar a reativação no Diário de Bordo da nota

### Espelhamento Diário
Apenas itens com `status: em-andamento` (de qualquer `type`) podem ter tarefas espelhadas no diário. Itens com `status: planejado` ficam exclusivamente em `Ativo/` e podem ser mencionados na seção `# Notas` do diário como referência.

### Conclusão e Arquivamento
1. Mover o arquivo de `Ativo/` para `Arquivo/`
2. Alterar `status` para `concluído` (ou `descontinuado`)
3. Remover da seção ativa do `index.md`
4. Registrar no logs.md
