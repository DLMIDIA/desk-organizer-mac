# 🧹 Desk Organizer Mac — Organizador Inteligente de Mesa & Downloads

> **Automação inteligente e nativa para macOS que organiza instantaneamente sua Área de Trabalho (Desktop) e pasta Downloads em categorias limpas, estruturadas e produtivas.**

Desenvolvido por **Daniel Júnior Barbosa da Silva (DL MIDIA)** em coautoria com **Antigravity AI**.

---

[![Platform](https://img.shields.io/badge/Platform-macOS%20(Sonoma%20%7C%20Sequoia)-000000?style=flat-square&logo=apple)](https://apple.com)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)](https://python.org)
[![AppleScript](https://img.shields.io/badge/Integration-AppleScript%20%26%20Notification%20Center-orange?style=flat-square)](https://developer.apple.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

---

## 📌 Visão Geral

Manter a Mesa e a pasta de Downloads organizadas no macOS pode consumir horas preciosas de designers, editores, gestores de tráfego e desenvolvedores.

O **Desk Organizer Mac** classifica e move arquivos em segundo plano com segurança (evitando sobrescrita acidental e respeitando downloads em andamento), agrupando tudo em 7 categorias principais:

```
Desktop/
├── 01 - Projetos & Sistemas/          # Repositórios, scripts .py, sites, apps
├── 02 - Orçamentos & Contratos/       # Propostas comerciais, orçamentos, minutas
├── 03 - Fotos, Vídeos & Drone/        # Mídias soltas, gravações, fotos brutas (RAW)
├── 04 - Design & Artes/               # Editáveis (PSD, PSB, AI, Figma) e peças
├── 05 - Documentos & PDFs/            # Planilhas, PDFs, documentos de texto
├── 06 - Capturas e Gravações de Tela/ # Prints e gravações de tela da Apple
└── 07 - Backups & Arquivos/           # Instaladores (.dmg, .pkg), compactados (.zip)
```

E para a pasta `~/Downloads`:
- **Instaladores e Compactados** (`.dmg`, `.pkg`, `.zip`, `.rar`)
- **Documentos e PDFs** (`.pdf`, `.xlsx`, `.docx`)
- **Imagens e Fotos** (`.png`, `.jpg`, `.webp`)
- **Vídeos e Mídias** (`.mp4`, `.mov`, `.mp3`)
- **Design e Vetores** (`.psd`, `.ai`, `.svg`)
- **Códigos e Scripts** (`.py`, `.js`, `.json`)

---

## ✨ Funcionalidades Principais

1. **Classificação Heurística Profunda:**
   - Detecta e agrupa não apenas por extensão, mas pelo nome do arquivo (ex: "Captura de Tela", "Gravação de Tela", "Orçamento", "Contrato").
   - Inspeciona o interior de pastas para categorizar projetos de código, pastas de design ou gravações de drone.
2. **Segurança Antissubscrição (`safe_move`):**
   - Se um arquivo de mesmo nome já existir no destino, adiciona sufixo numérico progressivo (ex: `relatorio (1).pdf`), impedindo qualquer perda de dados.
3. **Respeito a Downloads Ativos:**
   - Detecta extensões temporárias (`.crdownload`, `.download`, `.part`, `.tmp`) e aguarda a conclusão antes de mover.
4. **Notificação Nativa no macOS:**
   - Emite notificação no Centro de Notificações com som do sistema (*Glass*) ao finalizar a limpeza.
5. **Aplicativo Nativo na Área de Trabalho:**
   - Pode ser empacotado como `Organizar Mesa.app` para acionamento com 2 cliques ou atalho de teclado.

---

## 🚀 Como Usar

### Execução Direta via Terminal
```bash
# Para organizar a Mesa:
python3 organizar_mesa.py

# Para organizar Downloads:
python3 organizar_downloads.py

# Para organizar ambos de uma vez:
python3 organizar_tudo.py
```

### Compilar o Aplicativo Nativo (`.app`)
```bash
./build_app.sh
```
O arquivo **`Organizar Mesa.app`** será gerado diretamente na sua Mesa!

---

## 👨‍💻 Autores & Créditos

- **Autor:** Daniel Júnior Barbosa da Silva
- **Empresa / Marca:** [DL MIDIA](https://dlmidia.com.br)
- **Coautoria:** Antigravity AI (Google DeepMind)
- **Licença:** [MIT License](LICENSE)
