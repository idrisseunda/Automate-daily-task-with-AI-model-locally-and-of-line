# Getting started: the complete setup path

These guides use Linux commands and keep the work in a user-owned demo folder. Copy commands one at a time into a terminal. Software and model downloads require internet access; once downloaded, local model inference can run without a cloud model.

## 1. Install and test Ollama

Follow [Install Ollama](setup/OLLAMA.md). The short path is:

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2:3b
ollama run llama3.2:3b
```

At the model prompt, type a question. Type `/bye` to exit. Keep the exact model tag handy; the other applications need it too.

## 2. Pick an interface

- For a browser chat and document Q&A, follow [Install Open WebUI](setup/OPEN_WEBUI.md) and [connect it to Ollama](connect/OLLAMA_OPEN_WEBUI.md).
- For coding help inside an editor, follow [Install VS Code and Continue](setup/CONTINUE_VSCODE.md) and [connect Continue to Ollama](connect/OLLAMA_CONTINUE.md).
- For an agent that can work with files, follow [Install OpenClaw](setup/OPENCLAW.md) and [connect it to Ollama](connect/OLLAMA_OPENCLAW.md). Use the disposable workspace in the demo instructions.

## 3. Reproduce a demo

Start with the [local chat demo](demos/01-local-chat.md), then follow the matching guide for documents, business calculations, coding, file operations, or performance measurement. Each demo identifies the prerequisites, commands, expected result, and cleanup.

## 4. Python dependency

The Ollama helper scripts use Python's standard library. `analyze_sales.py` needs pandas, and JupyterLab opens the notebook. Install these in a virtual environment:

```bash
cd /path/to/local-ai-guide-cits
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Links to current vendor instructions

- [Ollama on Linux](https://ollama.com/download/linux)
- [Open WebUI quick start](https://docs.openwebui.com/getting-started/quick-start/)
- [Continue with Ollama](https://docs.continue.dev/customize/model-providers/top-level/ollama)
- [OpenClaw onboarding](https://docs.openclaw.ai/start/wizard)

If an application's menus or requirements differ from these notes, use the linked official documentation for the version you installed.
