# Configuracao Local do Ambiente

Este arquivo e um exemplo para instalacoes privadas. Copie para `.agents/assistant/local.md` quando precisar declarar regras locais que nao pertencem ao template publico.

`local.md` e ignorado pelo Git e pode conter taxonomias, dominios do diario, aliases, nomes de areas, convencoes de tags e outras preferencias do ambiente de uso.

## Taxonomia Local

Declare aqui apenas tags que fazem sentido para a sua instancia do cofre. O agente deve preservar tags existentes e so criar novas tags locais quando esta configuracao ou o usuario pedir explicitamente.

Exemplo:

```markdown
- Tags de area permitidas: `area/<nome-definido-pelo-usuario>`
- Tags de tema permitidas: `tema/<nome-definido-pelo-usuario>`
```

## Diario

Declare aqui os cabecalhos H1 usados no template diario local e como tarefas avulsas devem ser posicionadas.

Exemplo:

```markdown
- Cabecalhos diarios: `# Dominio A`, `# Dominio B`, `# Notas`
- Quando o dominio nao estiver claro, registrar em `# Notas` e nao criar nova secao automaticamente.
```
