# Registro de Conversas e Decisões

Este arquivo rastreia e armazena o histórico de decisões e conversas de desenvolvimento sobre a infraestrutura e comportamento do assistente.

---

## [2026-07-09] Reforma LLM Wiki V2.1: Ativo como Painel de Raiz e Tags `papel/*`

### Alinhamento de Metas
Reduzir a mistura entre projetos/produtos acompanhaveis e notas filhas dentro de `Ativo/`, tornando o painel executivo mais limpo para uso humano e mais previsivel para agentes.

### Decisoes de Design
1. **`Ativo/` como Painel Executivo:** `Ativo/` passa a conter apenas itens raiz acompanhaveis (`papel/raiz`) que devem aparecer no `index.md`.
2. **`Arquivo/` como Biblioteca de Apoio:** Dossies, sub-hubs, artefatos de apoio e notas vivas subordinadas a uma raiz ficam em `Arquivo/` com `papel/filha`, mesmo quando ainda sao consultados frequentemente.
3. **Taxonomia `papel/*`:** Adotadas as tags `papel/raiz`, `papel/filha`, `papel/moc` e `papel/fonte` para separar o papel operacional da nota do seu `type` e `status`.
4. **MOCs com Papel Proprio:** Arquivos `*- MOC.md` passam a usar `papel/moc`, mantendo `Temas MOC.md` como indice de temas macro.
5. **Lint Atualizado:** O script `.agents/scripts/lint_vault.py` passa a validar que notas em `Ativo/` tenham `papel/raiz` e MOCs tenham `papel/moc`.
6. **Compatibilidade Codex:** `AGENTS.md` explicita que Codex opera o cofre lendo `AGENTS.md` e `.agents/`, sem depender do runtime do Antigravity.
7. **Higiene da Raiz:** A raiz do cofre deve conter apenas arquivos de navegacao/configuracao. Anexos soltos devem ir para `Arquivo/attachments/`; scripts auxiliares devem ir para `.agents/scripts/`.

---

## [2026-07-09] Reforma LLM Wiki V2: Contexto Recuperavel e Lint Portatil

### Alinhamento de Metas
Fazer o cofre funcionar melhor como LLM Wiki, reduzindo falhas de contexto causadas por indices incompletos, metadados ausentes e ausencia de verificacao mecanica. A prioridade desta etapa e melhorar a recuperacao de contexto por agentes com automacao assistida.

### Decisoes de Design
1. **`index.md` como Catalogo Ativo Obrigatorio:** Toda nota em `Ativo/` deve aparecer no indice com status e descricao de uma linha, tornando o indice o ponto de entrada confiavel para agentes.
2. **`description` Obrigatorio em Ativo e MOCs:** Notas ativas e arquivos `*- MOC.md` passam a exigir `description` no frontmatter para sustentar navegacao progressiva no estilo OKF.
3. **Protocolo de Recuperacao de Contexto:** `AGENTS.md` e `agy.md` agora exigem leitura do indice, busca textual com `rg`, abertura do hub/nota relevante e seguimento controlado de wikilinks antes de responder que falta contexto.
4. **Hubs Ativos no `index.md`:** Hubs operacionais como `Mestrado na Europa`, `Agy Obsidian`, `Italia - Hub de Candidatura`, `Financas Pessoais - Setup` e `Trabalho na Europa` sao pontos de entrada ativos, enquanto `Temas MOC.md` permanece como catalogo de referencias frias e MOCs arquivados.
5. **Lint Cross-Platform:** A auditoria mecanica passa a usar `.agents/scripts/lint_vault.py`, script Python sem dependencias externas, para rodar em Windows, Linux e macOS.

---

## [2026-07-08] Compatibilidade Operacional com Codex

### Alinhamento de Metas
Permitir que o Codex opere o cofre com as mesmas regras historicamente mantidas para o Antigravity, sem duplicar a arquitetura nem criar uma segunda fonte de verdade para o comportamento do assistente.

### Decisões de Design
1. **Criação de `AGENTS.md` na raiz:** Adicionado um arquivo de instruções específico para o Codex, traduzindo os papéis, regras de escrita, modelo de camadas e mapa de intenção do Antigravity para o formato consumível pelo Codex.
2. **Preservação da Fonte Canônica em `.agents/`:** O `AGENTS.md` atua como ponte operacional. As regras detalhadas continuam centralizadas em `.agents/assistant/agy.md`, `architecture.md`, `glossary.md` e nas skills locais.
3. **Tradução de Papéis:** O Codex passa a reconhecer dois modos de atuação: Operador (`agy`) para rotinas do cofre e Arquiteto para mudanças estruturais, mantendo o firewall cognitivo já documentado.
4. **Compatibilidade com Skills Locais:** O `AGENTS.md` instrui o Codex a ler e aplicar os arquivos `.agents/skills/<nome>/SKILL.md` antes de executar rotinas equivalentes às do Antigravity.

---

## [2026-06-30] Melhorias Inspiradas pelo Open Knowledge Format (OKF) do Google

### Alinhamento de Metas
Incorporar princípios do [Open Knowledge Format (OKF)](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) do Google Cloud para melhorar a legibilidade do cofre por agentes de IA e formalizar padrões de navegação progressiva que o cofre já praticava intuitivamente.

### Decisões de Design
1. **Campo `description` Opcional no Frontmatter:** Adicionado ao esquema de Obsidian Properties como campo opcional e não retroativo. Inspirado pelo campo homônimo do OKF, permite que agentes entendam o contexto de uma nota lendo apenas o frontmatter ou o `index.md`, sem abrir o corpo do documento.
2. **Seção "Estratégia de Navegação Progressiva" no `agy.md`:** Formaliza a ordem de leitura recomendada (`index.md` → nota do item → MOC temático → fontes originais) para que o agente resolva dúvidas no nível mais alto possível, preservando a janela de contexto.
3. **Princípio de Independência Produtor/Consumidor:** Adicionado à seção de Sincronização com o Disco, explicitando que notas criadas por humanos e por agentes usam o mesmo formato (Markdown + YAML) sem camada de tradução.
4. **Descrições Inline no `index.md`:** Cada entrada do índice agora inclui um resumo de uma linha, alinhado com o padrão de progressive disclosure do OKF.
5. **Documentação no `glossary.md`:** O campo `description` foi formalmente documentado com regras de uso e exemplo.

---

## [2026-06-26] Introdução do Domínio de Freelance (area/freelance)


### Alinhamento de Metas
Permitir a diferenciação de projetos e demandas profissionais sob o modelo de freelance das demandas da empresa principal do usuário (Evo, area/evo) e das atividades estritamente pessoais (area/pessoal), mantendo a flexibilidade e simplicidade do painel diário de tarefas sem inflá-lo com novas divisões visuais.

### Decisões de Design
1. **Nova Tag de Domínio (`area/freelance`):** Adicionada como um domínio válido no manual `agy.md` e na habilidade `create-item` para permitir filtros e listagens futuras de freelas.
2. **Mapeamento de Rollover:** As tarefas associadas a projetos com tag `area/freelance` serão agrupadas e migradas na seção `# Trabalho` da nota diária (compartilhando a visualização com `area/evo`), mantendo as seções do diário simples (apenas Pessoal e Trabalho).

---

## [2026-06-13] Extensão do dump-material: Resolução de DOI e Download de URLs

### Alinhamento de Metas
Ampliar a capacidade de captura e catalogação da skill `/dump-material`, permitindo que o usuário envie diretamente links DOI ou links diretos de PDFs da web, além de arquivos locais da Inbox.

### Decisões de Design
1. **Script de download unificado (`download_helper.py`):** Criado em Python para rodar como intermediário na skill de ingestão. Ele resolve DOIs via API do Unpaywall, baixa PDFs Open Access legais e extrai metadados estruturados. Também baixa diretamente arquivos de links de PDFs.
2. **Tratamento de Paywalls em DOIs:** Se o Unpaywall indicar que o artigo correspondente ao DOI está sob paywall (não Open Access), a skill cria uma referência textual estruturada com o título, autores e link externo do DOI no MOC correspondente, sem abortar a operação.
3. **Padrão de Nome de Arquivo:** Os PDFs baixados via DOI são nomeados de forma higienizada usando o título do artigo (ex: `When_Do_LLMs_Know_What_They_Know.pdf`), mantendo a consistência do cofre.

---

## [2026-06-13] Refatoração de Hierarquia: Temas Macro (MOCs) vs. Notas Específicas

### Alinhamento de Metas
Garantir que o arquivo `Temas MOC.md` na raiz liste apenas os temas macros (hubs) do cofre, e que notas de estudos específicos (como o roteiro de certificação ou estudos técnicos focados) fiquem aninhadas dentro do respectivo MOC temático, preservando uma estrutura limpa e de fácil indexação.

### Decisões de Design
1. **Nomenclatura Padronizada dos MOCs:** Adotado o sufixo ` - MOC` para todos os temas macro (ex: `Product Operations - MOC.md`, `LLMs - MOC.md`, `Product Management - MOC.md`). Isso permite distinguir visualmente e programaticamente uma nota de índice macro de uma nota de estudo ou artigo específico.
2. **Hierarquização Semântica de Itens:**
   - A nota `Certificação Product Ops.md` foi vinculada na nova seção `## Estudos e Notas Relacionados` do `Product Operations - MOC.md`.
   - O `LLMs - MOC.md` foi criado para centralizar e indexar as notas específicas `Estudo LLMs.md`, `Estudo LLM Wiki.md`, a pesquisa de agentes e os workflows do TCC.
   - Foram criados MOCs macros adicionais (`Product Management - MOC.md`, `Career-Ops - MOC.md`, `PKM & Aprendizado - MOC.md`) para abrigar notas avulsas correspondentes (`Discovery.md`, `Como Implementar o Portal Work in Finland...`, `How to take smart Notes.md`).
3. **Limpeza do Master MOC:** O arquivo `Temas MOC.md` foi atualizado para conter **apenas** links para as notas macro com o formato `[[Arquivo/[Nome do Tema] - MOC]]`, delegando a listagem de arquivos específicos para o corpo de cada MOC individual.
4. **Gestão Operacional de MOCs:** Formalizado no manual e na arquitetura que a responsabilidade diária de criar, atualizar e registrar MOCs (e o arquivo `Temas MOC.md`) pertence ao operador **agy** (via skills como `dump-material`), enquanto o Antigravity (Arquiteto) mantém as regras e a infraestrutura técnica.

---

## [2026-06-13] Ingestão de Referências: Skill dump-material e Master MOC

### Alinhamento de Metas
Criar um mecanismo eficiente de captura e arquivamento de referências externas (PDFs, links) que permita catalogação inteligente por temas sem inflar os painéis ativos do cofre e otimizando a performance dos subagentes.

### Decisões de Design
1. **Nova Skill `dump-material`:** O usuário aciona explicitamente para processar referências externas, movendo PDFs para `Fontes/` e associando-os a MOCs de temas.
2. **Separação de Conteúdo em Estudos Ativos:**
   - *Materiais externos:* Indexados imediatamente na seção `## Conceitos e Referencias` do MOC correspondente.
   - *Produção própria (notas, resumos, sínteses):* Mantidos em `Ativo/` até que o estudo seja concluído e movido para `Arquivo/`, momento em que o assistente consolida as anotações no MOC.
3. **Master MOC (`Temas MOC.md`):** Criado na raiz do cofre como índice central de MOCs ativos e arquivados. Ele serve como sumário e cache semântico para o subagente `theme-associator` consultar os temas disponíveis rapidamente, evitando buscas completas e caras no cofre.
4. **Simplificação de Estrutura:** Rejeitada a associação ou indexação de diretórios locais (como mapear caminhos no MOC), mantendo a filosofia de arquitetura plana.

---

## [2026-06-12] Reestruturação: Fusão Projetos/ + Temas/ → Ativo/

### Alinhamento de Metas
Simplificar a estrutura do cofre eliminando a separação artificial entre `Projetos/`, `Temas/` e `Fila de Ideias/`, fundindo tudo em uma única zona de trabalho ativa (`Ativo/`). Introduzir o conceito formal de `type: produto` para demandas contínuas que evoluem com melhorias.

### Decisões de Design
1. **Fusão de Pastas**: `Projetos/`, `Temas/` e `Fila de Ideias/` foram fundidos em `Ativo/`. A distinção entre tipos de item passa a ser semântica (via `type` no frontmatter), não organizacional (via pastas).
2. **Novo Tipo `produto`**: Introduzido para representar demandas contínuas (como Dashboard Produto) que não têm prazo final e recebem melhorias esporádicas. Ciclo: `em-andamento → em-manutenção ↔ em-andamento → descontinuado`.
3. **Glossário Formal**: Criado `.agents/assistant/glossary.md` como referência canônica de tipos, status e ciclos de vida.
4. **Skill Unificada**: `create-project` renomeada para `create-item`, suportando criação de projetos, produtos e estudos com templates adaptativos.
5. **Sem Emojis em Headings**: Convenção de não usar emojis em títulos de seção para manter legibilidade programática.
6. **Reativação**: Items concluídos em `Arquivo/` podem ser reativados movendo de volta para `Ativo/` quando surgirem novas demandas.

---

## [2026-06-11] Sessão de Transição para Habilidades Integradas

### Alinhamento de Metas
Substituição completa do script Python legado (`agy.py`) pela infraestrutura nativa de habilidades do Antigravity, estruturando o cofre segundo a lógica do **LLM Wiki**.

### Decisões de Design
1. **Limpeza Completa:** Descartada a pasta `.agy/` e qualquer código Python antigo. O projeto usará apenas as habilidades nativas do Antigravity.
2. **Separação de Contextos:**
   *   **Ambiente Técnico (IA):** Arquivos salvos em `.agents/assistant/` com nomenclatura compacta (minúsculo e sem espaços), sem frontmatter do Obsidian ou formatações wikilinks.
   *   **Ambiente Humano (Usuário):** Notas e temas localizados em `Temas/`, `Projetos/` e `Diario/` formatados de forma amigável com Obsidian Properties e links dinâmicos.
3. **Daily Rollup:** Lógica flexível que pula a migração silenciosamente se o diário de hoje não existir.
4. **Camada de Fontes Imutáveis:** Criação da pasta `Fontes/` onde os arquivos originais são arquivados após processados da inbox.
5. **Obsidian Properties:** Adoção de chaves modernas (`created`, `type`, `status`, `tags`, `project`, `links`).

---

## [2026-06-11] Implementação do Future Log Dinâmico

### Alinhamento de Metas
Incorporar a filosofia do "Future Log" do Bullet Journal nas notas diárias, minimizando o atrito da migração manual de prazos e eventos.

### Decisões de Design
1. **Prazos em Projetos:** Prazos não ficam soltos na root; eles são registrados nos cronogramas dos respectivos projetos.
2. **Rollup Dinâmico Total:** A skill `daily-digest` foi atualizada. O subagente rastreia todos os marcos futuros nos projetos ativos e os injeta na seção `# Eventos Futuros e Prazos` do novo diário.
3. **UI Minimalista:** Seção mantida slim, sem emojis, respeitando a estética do cofre.

---

## [2026-06-11] Separação de Papéis (Firewall Cognitivo)

### Alinhamento de Metas
Evitar "Esquizofrenia de Papéis" e alucinações sistêmicas ao separar a persona do Desenvolvedor da persona do Assistente Diário.

### Decisões de Design
1. **Separação Rígida:** Estabelecido o Firewall Cognitivo dividindo os papéis entre o Arquiteto (Antigravity) e o Operador (agy). As regras e responsabilidades detalhadas foram formalizadas no [architecture.md#👥-firewall-cognitivo-e-subagentes](file:///c:/Users/Gui.ABC/Documents/GitHub/obsidian/.agents/assistant/architecture.md#👥-firewall-cognitivo-e-subagentes).

---

## [2026-06-11] Revisão Comportamental do Agy — Ação Mínima e Espelhamento

### Alinhamento de Metas
Corrigir padrões de over-engineering do Agy identificados em sessão de análise de erros: o agente transformava capturas passivas em demandas ativas, inflava o diário com tarefas não priorizadas e inventava escopo em projetos em standby.

### Decisões de Design
1. **Princípio de Ação Mínima:** Regra formal no `agy.md` — executar exclusivamente o que foi pedido, sem ações complementares.
2. **Mapa de Intenção:** Tabela de referência para classificar pedidos do usuário (anotar ≠ criar tarefa ≠ criar projeto).
3. **Espelhamento Diário ↔ Projeto:** Apenas projetos `em-andamento` espelham tarefas no diário. Hierarquia: Domínio (Pessoal/Trabalho) → Projeto → Tarefas.
4. **Template Adaptativo em `create-project`:** Projetos `planejado` não possuem cronograma de execução. Nova seção obrigatória `💡 Motivação e Origem`.
5. **Regras de Mudança de Estado:** O Agy não promove status nem marca tarefas como concluídas sem confirmação explícita. "Não é uma demanda até o usuário dizer que é."

---

## [2026-06-11] Simplificação de Metadata — Tags Hierárquicas

### Alinhamento de Metas
Eliminar redundância no frontmatter (properties `domain` e `project` duplicavam informação já disponível via tags e links) e adotar o padrão da comunidade Obsidian de tags hierárquicas para classificação de domínio.

### Decisões de Design
1. **Remoção de `domain`:** Substituído pela tag `area/evo` (trabalho) ou `area/pessoal`. O Agy infere o domínio a partir das tags.
2. **Remoção de `project`:** Estava sempre vazio em projetos. Para notas que referenciam projetos, usar `links` ou wikilinks no corpo.
3. **Remoção de `projeto` das tags:** A tag genérica `projeto` era redundante com `type: projeto` no frontmatter.
4. **Adoção de tags hierárquicas:** `status/planejado`, `area/evo`, `area/pessoal` — seguindo o padrão consolidado da comunidade Obsidian.
5. **Properties mantidas:** `created`, `type`, `status`, `tags`, `links` — dados tipados que o agente lê programaticamente.
6. **Fontes de referência:** Comunidade Obsidian (tags hierárquicas `area/`, `status/`, `type/`), LLM Wiki (metadata mínimo para agentes), Bullet Journal (simplicidade, nota ≠ tarefa).


