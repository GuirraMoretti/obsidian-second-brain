# Registro de Decisoes Arquiteturais

Este arquivo guarda decisoes estruturais do template publico. Historico, nomes de projetos, tags e exemplos de uma instancia privada do cofre nao devem ser registrados aqui.

---

## [2026-07-09] Template Publico: Taxonomia Local Fora do Prompt

### Alinhamento de Metas

Preparar a estrutura do cofre para uso como template publico e open source, removendo referencias pessoais e evitando que o agente imponha tags, areas, dominios ou categorias que pertencem ao ambiente de uso.

### Decisoes de Design

1. **Template sem dados pessoais:** Manuais, skills, README e arquivos de configuracao do agente devem usar exemplos neutros e placeholders genericos.
2. **Taxonomia local e privada:** Tags de conteudo como `area/*`, `tema/*`, categorias e dominios do diario nao fazem parte do contrato publico do template.
3. **Responsabilidade do agente limitada:** O agente pode manter metadados estruturais necessarios ao funcionamento do template, como `status/*` e `papel/*`, mas nao deve criar, migrar, renomear ou validar taxonomias livres sem instrucao explicita.
4. **Configuracao por ambiente:** Instalacoes privadas podem declarar convencoes locais em `.agents/assistant/local.md`, arquivo ignorado pelo Git. O template publica apenas `.agents/assistant/local.example.md`.
5. **Diario guiado pelo template local:** O agente deve preservar os cabecalhos existentes no diario/template da instancia. Se a secao correta nao estiver clara, deve registrar em `# Notas` ou perguntar antes de criar novo dominio.

---

## [2026-07-09] LLM Wiki: Ativo como Painel de Raiz

### Alinhamento de Metas

Separar itens acompanhaveis de materiais de apoio, tornando o painel ativo previsivel para uso humano e por agentes.

### Decisoes de Design

1. **`Ativo/` como painel executivo:** Contem apenas itens raiz acompanhaveis (`papel/raiz`) que devem aparecer no `index.md`.
2. **`Arquivo/` como biblioteca de apoio:** Dossies, sub-hubs, artefatos de apoio e notas subordinadas ficam em `Arquivo/` com `papel/filha`.
3. **Papeis operacionais:** `papel/raiz`, `papel/filha`, `papel/moc` e `papel/fonte` separam a funcao operacional da nota de seu `type` e `status`.
4. **MOCs como indices tematicos:** Arquivos `*- MOC.md` usam `papel/moc` e sao listados no `Temas MOC.md`.
5. **Lint portatil:** `.agents/scripts/lint_vault.py` valida navegabilidade basica, links, metadados estruturais e higiene da raiz.

---

## [2026-07-08] Compatibilidade Operacional com Codex

### Alinhamento de Metas

Permitir que o Codex opere o cofre com as mesmas regras do assistente historico, sem duplicar a fonte de verdade.

### Decisoes de Design

1. **`AGENTS.md` na raiz:** Traduz papeis, regras de escrita, modelo de camadas e mapa de intencao para o formato consumivel pelo Codex.
2. **Fonte canonica em `.agents/`:** Regras detalhadas continuam centralizadas em `.agents/assistant/` e `.agents/skills/`.
3. **Papeis separados:** Codex atua como Operador para rotinas do cofre e como Arquiteto apenas para mudancas estruturais.
4. **Skills locais:** O Codex deve ler o `SKILL.md` correspondente antes de executar rotinas equivalentes.

---

## [2026-06-30] Contexto Recuperavel e Lint

### Alinhamento de Metas

Melhorar a recuperacao de contexto por agentes, reduzindo falhas causadas por indices incompletos, metadados ausentes e falta de verificacao mecanica.

### Decisoes de Design

1. **`index.md` como catalogo ativo:** Toda nota em `Ativo/` deve aparecer no indice com status e descricao de uma linha.
2. **`description` obrigatorio:** Notas em `Ativo/` e MOCs exigem uma descricao curta no frontmatter.
3. **Protocolo de recuperacao:** Agentes devem ler o indice, buscar termos relevantes, abrir a nota/MOC mais relevante e seguir somente wikilinks diretamente relacionados.
4. **Higiene da raiz:** A raiz deve conter apenas arquivos de navegacao e configuracao. Anexos vao para `Arquivo/attachments/`; scripts auxiliares vao para `.agents/scripts/`.

---

## [2026-06-12] Estrutura Base do Cofre

### Alinhamento de Metas

Simplificar a organizacao do cofre em camadas claras, usando Markdown, Obsidian Properties e skills locais para rotinas repetiveis.

### Decisoes de Design

1. **Camadas principais:** `Inbox/`, `Fontes/`, `Ativo/`, `Diario/`, `.agents/` e `Arquivo/`.
2. **Tipos de nota:** `projeto`, `produto`, `estudo`, `ideia`, `fonte` e `diario`.
3. **Status padronizados:** `planejado`, `em-andamento`, `em-manutenção`, `concluído`, `descontinuado`, `pendente` e `arquivado`.
4. **Skills operacionais:** `capture-idea`, `create-item`, `process-inbox`, `daily-digest`, `dump-material`, `lint-vault` e `vault-sync`.
5. **Acao minima:** O agente executa o que foi solicitado, sem transformar registros passivos em tarefas ou promover status sem sinal claro do usuario.
