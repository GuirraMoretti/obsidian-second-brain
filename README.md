# 🧠 Segundo Cérebro — Template de Wiki Pessoal com IA (Obsidian + Antigravity)

Um sistema completo de **base de conhecimento pessoal** (Second Brain / Personal Knowledge Management) que utiliza **Obsidian** como editor e o assistente de IA **Antigravity** como copiloto inteligente para organizar, curar e manter suas notas, projetos e estudos.

> **O que torna este projeto diferente?** Este não é apenas um template de notas — é um **sistema operacional de produtividade** com 7 habilidades de IA que automatizam a captura de ideias, organização de inbox, gestão de projetos, auditoria de consistência e sincronização com GitHub.

---

## ✨ Features

- 📥 **Captura rápida de ideias** — Dite ideias no chat e elas viram notas estruturadas automaticamente
- 📋 **Processamento inteligente de Inbox** — Notas brutas são classificadas, enriquecidas com metadados e organizadas
- 📅 **Digest diário automático** — Migração de tarefas pendentes, consolidação de notas e rastreamento de prazos
- 📁 **Criação estruturada de itens** — Projetos, produtos e estudos com templates adaptativos por tipo e status
- 📚 **Ingestão de materiais** — Catalogação de PDFs e artigos em MOCs (Maps of Content) temáticos
- 🔍 **Auditoria de saúde** — Detecção de links quebrados, notas órfãs, contradições e conceitos não mapeados
- 🔄 **Sincronização com GitHub** — Push/Pull com resolução autônoma de conflitos para uso multi-dispositivo

---

## 📂 Estrutura de Pastas (Modelo de 5 Camadas)

| Camada | Pasta | Descrição |
| :--- | :--- | :--- |
| **Camada 0** | `Inbox/` | Buffer temporário para capturas rápidas e rascunhos |
| **Camada 1** | `Fontes/` | Arquivo de documentos originais (PDFs, imagens). Imutável. |
| **Camada 2** | `Ativo/` | Wiki ativa — projetos, produtos e estudos em foco |
| **Camada 2** | `Diario/` | Notas diárias com tarefas, notas e prazos |
| **Camada 3** | `.agents/` | Configuração e habilidades do assistente de IA |
| **Camada 4** | `Arquivo/` | Histórico — itens concluídos ou desativados |

---

## 🚀 Setup Rápido

### Pré-requisitos

- [Obsidian](https://obsidian.md/) instalado
- [Antigravity](https://antigravity.google/) configurado (IDE com suporte a agentes de IA)

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SEU-USUARIO/obsidian-second-brain.git
   ```

2. **Abra no Obsidian:**
   - Abra o Obsidian → "Open folder as vault" → selecione a pasta clonada
   - Habilite a visualização de **Properties** (Configurações > Editor > Properties in document > Visible)

3. **Configure o Antigravity:**
   - Abra o projeto no Antigravity
   - Os agentes e skills em `.agents/` serão detectados automaticamente

4. **Personalize:**
   - Edite o `index.md` para adicionar seus projetos e estudos
   - Comece capturando ideias ou criando itens via chat com o assistente

---

## 🤖 Habilidades do Assistente (Skills)

| Skill | Comando | Descrição |
| :--- | :--- | :--- |
| **capture-idea** | *"Capture a ideia: [título]"* | Salva uma ideia rápida na `Inbox/` com metadados estruturados |
| **create-item** | *"Crie o projeto [nome]"* | Cria projetos, produtos ou estudos em `Ativo/` com template adaptativo |
| **process-inbox** | *"Processe a inbox"* | Triagem e organização de notas brutas da `Inbox/` |
| **daily-digest** | *"Faça o daily digest"* | Consolida o dia, migra tarefas e extrai conhecimento das notas |
| **dump-material** | *"Catalogue este artigo: [URL/DOI]"* | Ingere PDFs/artigos e categoriza em MOCs temáticos |
| **lint-vault** | *"Faça o lint do cofre"* | Auditoria de saúde: links quebrados, órfãs, contradições |
| **vault-sync** | *"Suba para o GitHub"* | Sincronização Git com resolução autônoma de conflitos |

---

## 🔄 Fluxo de Trabalho Diário

```
1. 📥 Capture ideias → Inbox/
2. 📋 Processe a inbox → Ativo/ ou Arquivo/
3. ✅ Gerencie tarefas → Diario/Daily/
4. 🔄 Daily digest → Migração e consolidação
5. 📚 Catalogue materiais → MOCs em Arquivo/
6. 🔍 Audit periódico → lint-vault
```

---

## 🏷️ Padrões de Metadados

Todas as notas utilizam **Obsidian Properties** (YAML frontmatter):

```yaml
---
created: 2026-01-15
type: projeto       # projeto, produto, estudo, ideia, fonte, diario
status: em-andamento # planejado, em-andamento, em-manutenção, concluído, descontinuado, pendente, arquivado
tags:
  - status/em-andamento
  - area/pessoal     # area/pessoal, area/evo (trabalho), area/freelance
links:
  - "[[NotaRelacionada]]"
---
```

### Tipos de Item

| Tipo | Descrição | Exemplo |
| :--- | :--- | :--- |
| `projeto` | Iniciativa finita com prazo e entrega | Projeto de formatura, migração de sistema |
| `produto` | Demanda contínua que evolui | Dashboard, ferramenta interna |
| `estudo` | Tema de aprendizado ou pesquisa | Estudo de IA, certificação |
| `ideia` | Conceito capturado, sem forma definida | Insight, brainstorm |

---

## 🏗️ Arquitetura do Assistente

O sistema implementa um **Firewall Cognitivo** com separação de papéis:

- **Antigravity (Arquiteto):** Agente principal que configura e mantém a infraestrutura em `.agents/`
- **agy (Operador):** Subagente especializado nas rotinas diárias do cofre (Inbox, Ativo, Diário)
- **Subagentes especializados:** `notes-consolidator`, `project-tracker`, `theme-associator` — instanciados sob demanda pelas skills

Documentação completa da arquitetura em [`.agents/assistant/`](.agents/assistant/).

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 🙏 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias nas skills, novos templates ou correções.

---

> *"Um segundo cérebro não é sobre guardar tudo — é sobre guardar o que importa, no lugar certo, de forma que você encontre quando precisar."*
