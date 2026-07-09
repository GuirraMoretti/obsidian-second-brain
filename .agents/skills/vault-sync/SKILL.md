---
name: vault-sync
description: Sincroniza o cofre Obsidian com o repositório remoto no GitHub. Suporta dois modos — "indo" (push) e "voltando" (pull) — e resolve conflitos automaticamente sem precisar de intervenção do usuário.
---

# Habilidade: Sincronização com o Repositório Remoto (vault-sync)

Esta habilidade gerencia o ciclo completo de sincronização do cofre com o GitHub, cobrindo tanto o envio de atualizações locais quanto a recepção de mudanças remotas, com resolução autônoma de conflitos.

> **Contexto de uso:** O cofre é utilizado em múltiplos workspaces (computadores/usuários diferentes) que fazem commits independentes. Por isso, o remoto pode sempre estar à frente do local — o fluxo de PUSH **sempre** busca as atualizações remotas antes de subir, nunca assumindo que o local é o mais recente.

## Identificação do Modo

O assistente deve inferir o modo pela intenção do usuário:
- **Modo PUSH ("indo")**: Usuário quer enviar o estado atual do cofre para o remoto. Palavras-chave: *"upar"*, *"push"*, *"subir"*, *"enviar"*, *"indo"*, *"atualizar remoto"*.
- **Modo PULL ("voltando")**: Usuário quer trazer atualizações do remoto para o local. Palavras-chave: *"pull"*, *"puxar"*, *"baixar"*, *"voltando"*, *"sincronizar"*, *"trazer"*.
- **Modo FULL SYNC**: Usuário quer os dois. Palavras-chave: *"sync completo"*, *"sincronizar tudo"*, *"pull e push"*.

---

## Modo PUSH ("indo")

Execute os passos abaixo **em sequência**, tratando cada erro antes de avançar:

### 1. Verificar Estado do Repositório
Execute `git status` para inspecionar o estado atual.

### 2. Detectar Conflitos de Merge Pendentes
Se `git status` mostrar arquivos em estado `both modified` ou `unmerged`:
- Execute `git diff --name-only --diff-filter=U` para listar os arquivos em conflito.
- Para cada arquivo em conflito, aplique a **Estratégia de Resolução Autônoma** (seção abaixo).
- Após resolver, execute `git add <arquivo>` para cada arquivo resolvido.

### 3. Guardar Mudanças Locais em Stash (SEMPRE)
Independentemente de o remoto estar à frente ou não, **sempre** execute o stash se houver qualquer mudança local (staged ou unstaged) ainda não commitada. Isso protege o trabalho local durante o rebase:
- Execute `git stash push --include-untracked -m "vault-sync: stash antes do pull"`.
- Se não houver nada para guardar (`No local changes to save`), prossiga sem stash.

### 4. Pull com Rebase (SEMPRE, antes de qualquer push)
Este passo é **obrigatório** e incondicional. Como o cofre é usado em múltiplos workspaces, o remoto pode ter commits novos a qualquer momento — nunca assuma que o local é o mais recente.

Execute `git pull --rebase origin main`.
- Se o pull retornar `Already up to date`: ótimo, prossiga.
- Se houver conflitos durante o rebase, aplique a **Estratégia de Resolução Autônoma** arquivo a arquivo.
- Após resolver cada conflito: `git add <arquivo>` e depois `git rebase --continue`.
- Se o rebase travar irrecuperavelmente: execute `git rebase --abort`, restaure o stash com `git stash pop` e tente `git pull --no-rebase origin main` como fallback de merge direto.

### 5. Restaurar Stash (se aplicável)
Se tiver feito stash no passo 3, execute `git stash pop`.
- Se o stash pop gerar conflitos, aplique a **Estratégia de Resolução Autônoma** para cada arquivo conflitante.

### 6. Montar a Mensagem de Commit
Inspecione os arquivos modificados com `git status` para construir uma mensagem de commit descritiva e concisa no formato:
```
sync: <Resumo das mudanças principais>
```
Exemplos:
- `sync: Diário 26-06-2026, notas consolidadas e updates de projetos`
- `sync: Captura de ideias e atualização do Formatura UFC`

Se não houver nada para commitar (working tree limpa após o rebase), informe o usuário que o cofre já estava sincronizado e encerre.

### 7. Commit e Push
```
git add .
git commit -m "<mensagem gerada>"
git push origin main
```
Se `git push` falhar com `rejected` (outro workspace subiu algo entre o passo 4 e agora): repita os passos 4→5→7 imediatamente, sem stash novamente.

---

## Modo PULL ("voltando")

### 1. Verificar Estado Local
Execute `git status`. Se houver mudanças locais não commitadas:
- Execute `git stash push -m "vault-sync: stash antes do pull"`.

### 2. Pull
Execute `git pull origin main`.

### 3. Resolver Conflitos (se houver)
Se o pull gerar conflitos:
- Execute `git diff --name-only --diff-filter=U` para listar os conflitos.
- Aplique a **Estratégia de Resolução Autônoma** para cada arquivo.
- Execute `git add <arquivo>` após cada resolução.
- Execute `git commit -m "sync: Resolve conflitos do pull"`.

### 4. Restaurar Stash (se aplicável)
Execute `git stash pop`.
- Se o stash pop gerar conflito, aplique a **Estratégia de Resolução Autônoma** novamente.

---

## Estratégia de Resolução Autônoma de Conflitos

Ao encontrar marcadores de conflito (`<<<<<<<`, `=======`, `>>>>>>>`), siga esta lógica por tipo de arquivo:

### Notas Diárias (`Diario/Daily/*.md`)
- **Seções de tarefas (`# Tarefas Pessoais`, `# Trabalho`)**: Mescle as duas versões, mantendo **todas** as tarefas de ambas as partes sem duplicatas.
- **Seção `# Notas`**: Concatene as anotações de ambas as versões.
- **Seção `# Eventos Futuros e Prazos`**: Mescle e reordene cronologicamente.
- **Seção `# Impedimentos de Projetos`**: Mescle, mantendo todos os impedimentos.
- **Frontmatter (YAML)**: Prefira sempre a versão local (`HEAD`).

### Arquivos de Projetos/Produtos (`Ativo/*.md`, `Arquivo/*.md`)
- **Frontmatter (YAML)**: Prefira a versão com `status` mais avançado (ex: `em-andamento` > `planejado` > `pendente`). Em caso de dúvida, prefira `HEAD`.
- **Seção `## Diario de Bordo`**: Mescle **todas** as entradas de ambas as versões, ordenadas por data.
- **Checklists (`- [ ]`, `- [x]`)**: Prefira `- [x]` (tarefa concluída) sobre `- [ ]` quando a mesma tarefa aparece em ambas as versões.
- **Demais seções**: Prefira a versão local (`HEAD`) e adicione conteúdo novo do remoto ao final da seção.

### Arquivo de Logs (`.agents/assistant/logs.md`)
- Mescle todas as entradas de ambas as versões, mantendo a ordem cronológica.

### Arquivo `index.md`
- Prefira a versão local (`HEAD`) como base e incorpore linhas novas do remoto que não existam localmente.

### Regra Geral (fallback)
Para qualquer arquivo não coberto acima:
- Use `git checkout --ours <arquivo>` (prefere versão local) como fallback seguro.
- Documente no log o arquivo que precisou de resolução por fallback.

---

## Log e Feedback

Ao final da execução, informe ao usuário:
- **Modo executado**: PUSH, PULL ou FULL SYNC.
- **Arquivos sincronizados**: Lista resumida.
- **Conflitos resolvidos**: Se houve algum, quais arquivos e como foram resolvidos.
- **Resultado final**: Confirmação de sucesso ou descrição do problema se algo falhar.

Registre silenciosamente no `.agents/assistant/logs.md` no formato:
```
## [AAAA-MM-DD] sync | Modo: [PUSH/PULL/FULL] | [N] arquivos | Conflitos: [Sim/Não]
```
