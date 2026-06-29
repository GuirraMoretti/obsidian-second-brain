# Referências da Plataforma Antigravity

Guia rápido para consultar a documentação oficial ao fazer manutenção arquitetural no cofre.

---

## Onde buscar documentação

O site oficial (https://antigravity.google) é uma SPA e não renderiza conteúdo via fetch direto. Use estas alternativas:

- **Docs oficiais (via browser):** https://antigravity.google/docs/skills e https://antigravity.google/docs/agents
- **Blog oficial:** https://blog.google/technology/google-deepmind/antigravity/
- **Queries de busca que funcionam:**
  - `Google Antigravity IDE skills SKILL.md subagents define_subagent invoke_subagent documentation`
  - `Google Antigravity agent skills folder ".agents" SKILL.md best practices`
  - `Antigravity define_subagent system prompt workspace inherit branch`

---

## Conceitos-chave da plataforma

### Skills (`.agents/skills/<nome>/SKILL.md`)
- O agente usa `name` e `description` do **frontmatter YAML** para decidir se aciona a skill (Discovery).
- O corpo do SKILL.md só é lido quando selecionado (Progressive Disclosure).
- Manter abaixo de ~500 linhas. Conteúdo pesado vai em subpastas.
- Estrutura de pastas suportada:
  ```
  skill-name/
  ├── SKILL.md           # Instruções principais (obrigatório)
  ├── scripts/           # Scripts auxiliares
  ├── references/        # Documentação complementar, schemas, prompts de subagentes
  ├── examples/          # Exemplos de uso
  └── assets/            # Templates, imagens, configs
  ```

### Subagentes (`define_subagent` + `invoke_subagent`)
- Instâncias autônomas com **contexto isolado** (não herdam histórico do pai).
- Definidos em runtime via `define_subagent(name, system_prompt, tools)`.
- Invocados via `invoke_subagent(name, prompt)`.
- Modos de workspace: `inherit` (mesmo workspace), `branch` (isolado), `share` (compartilhado).
- Subagentes NÃO precisam de SKILL.md — são definidos programaticamente. Mas seus prompts devem ser documentados em `references/` para consistência entre sessões.

### Comunicação entre agentes
- `send_message(recipient, message)` para enviar instruções a um subagente em execução.
- O sistema notifica automaticamente quando um subagente termina (sem polling).

---

## Checklist para manutenção arquitetural

Antes de alterar qualquer arquivo em `.agents/`:

1. Consultar este arquivo para relembrar os mecanismos nativos.
2. Ler [decisions.md](decisions.md) para não repetir erros passados.
3. Ler [architecture.md](architecture.md) para entender o estado atual.
4. Verificar se a mudança cria redundância (informação duplicada em múltiplos arquivos).
5. Após a mudança, registrar a decisão em [decisions.md](decisions.md).
