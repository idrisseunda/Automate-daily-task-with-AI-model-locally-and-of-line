# Offline AI: From Private Chat to Coding and Agents

A Linux-first, step-by-step project for installing Ollama and connecting a local model to Open WebUI, VS Code with Continue, and OpenClaw. It includes separate setup guides, integration guides, demo walkthroughs, and runnable Python examples.

> **Start here:** work through [the getting-started path](docs/GETTING_STARTED.md). Download software and models while online before attempting an offline demonstration.

## Choose what you want to do

### Install a tool

- [Install Ollama and download a model](docs/setup/OLLAMA.md)
- [Install Open WebUI](docs/setup/OPEN_WEBUI.md)
- [Install VS Code and Continue](docs/setup/CONTINUE_VSCODE.md)
- [Install OpenClaw](docs/setup/OPENCLAW.md)

### Connect Ollama to an application

- [Ollama + Open WebUI](docs/connect/OLLAMA_OPEN_WEBUI.md)
- [Ollama + VS Code + Continue](docs/connect/OLLAMA_CONTINUE.md)
- [Ollama + OpenClaw](docs/connect/OLLAMA_OPENCLAW.md)

### Follow a complete demo

- [01 — Chat with a local model](docs/demos/01-local-chat.md)
- [02 — Ask questions about a local document](docs/demos/02-document-questions.md)
- [03 — Analyze fictional sales data with Python](docs/demos/03-business-sales.md)
- [04 — Use Continue to explain and edit code](docs/demos/04-vscode-coding.md)
- [05 — Let OpenClaw work in a dedicated demo folder](docs/demos/05-openclaw-files.md)
- [06 — Measure model speed and context use](docs/demos/06-performance.md)

## Project files

- `offline-ai-guide.ipynb` — original workshop flow, with presenter-only notes removed.
- `analyze_sales.py` — reusable sales analysis program.
- `scripts/create_sample_sales.py` — creates fictional input data for the sales demo.
- `scripts/ollama_status.py` — checks local Ollama and lists installed/loaded models.
- `scripts/ollama_context_sweep.py` — optional context-size measurement for one local model.
- `scripts/ollama_speed_benchmark.py` — optional token-speed measurement for installed models.
- `requirements.txt` — pandas and JupyterLab for the notebook and analysis script.

## Requirements and expectations

- Linux is the documented path. Commands may differ on macOS or Windows; follow the linked official installation pages for those systems.
- A working internet connection is needed to install applications and download model weights. Once everything required is downloaded and configured, the local chat and coding examples can be run without a cloud model. Open WebUI document retrieval needs its own local parser/embedding setup; see its [offline guide](https://docs.openwebui.com/tutorials/maintenance/offline-mode/).
- Start with a small model that fits your computer. Model size, speed, and available features depend on RAM, GPU memory, quantization, and context length.
- OpenClaw can use tools that read or change files. Use a disposable demo directory, keep its gateway private, review tool permissions, and verify changes. Do not give a new agent access to personal or business folders.
- The sales data is fictional. The scripts compute arithmetic; they do not provide business advice.

## Python setup

From the repository directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Open the notebook with Jupyter using this environment, or run the standalone Python commands shown in the demo guides.

## Official documentation

The setup guides link to upstream installation and configuration instructions. Software interfaces and requirements can change, so use those links to check current version-specific details.
