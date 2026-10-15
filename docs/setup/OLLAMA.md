# Install Ollama and download a local model

Ollama is the local model runtime used by the other project guides. The Linux installer is published by Ollama; it installs the runtime and normally starts its service.

## Before you begin

- Linux computer with a supported CPU, and optionally a compatible GPU.
- Internet connection for the installer and model download.
- Several gigabytes of free disk space. Model memory needs vary; begin with a small model.

## Install

In a terminal, run the current official Linux install command:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

The installer may ask for your password to configure the system service. If you prefer to inspect the installer before running it, open [Ollama's Linux installation page](https://ollama.com/download/linux) and follow its manual steps.

Check that the command is available:

```bash
ollama --version
```

Check the service:

```bash
systemctl status ollama
```

On a system where the service is installed but stopped, start it with:

```bash
sudo systemctl start ollama
```

If your installation does not use systemd, start the server in its own terminal with `ollama serve` and leave that terminal open.

## Download and run the example model

The workshop uses `qwen3:8b` as a modest first model. The actual speed and whether it fits depend on your computer.

```bash
ollama pull qwen3:8b
ollama list
ollama run qwen3:8b
```

At the `>>>` prompt, ask a question such as:

```text
Explain what a local language model does in two sentences.
```

Exit the model prompt with `/bye`. `ollama run` downloads a missing model automatically, but the explicit `pull` step makes the download clear before an offline demo.

## Verify the local API

Ollama's local API normally listens on port 11434:

```bash
curl http://127.0.0.1:11434/api/tags
```

The response should list the model you downloaded. You can also run this repository's diagnostic:

```bash
python scripts/ollama_status.py
```

## Download another model

Choose the model and exact tag from the [Ollama model library](https://ollama.com/library), then download it with `ollama pull MODEL:TAG`. Use that exact tag in Continue or OpenClaw. Model sizes and tags change over time.

## Helpful commands

```bash
ollama list       # models stored on disk
ollama ps         # models currently loaded in memory
ollama stop llama3.2:3b
```

## Troubleshooting

- `ollama: command not found`: open a new terminal; if it remains unavailable, revisit the official installer instructions.
- Connection refused on port 11434: start the Ollama service or run `ollama serve` in another terminal.
- Model fails to load: try a smaller model, close other GPU-heavy programs, or lower the context size in the client.
- Download fails: check internet access and free disk space. Download all required models before disconnecting from the internet.

Official links: [Linux installation](https://ollama.com/download/linux), [model library](https://ollama.com/library), [API documentation](https://github.com/ollama/ollama/blob/main/docs/api.md).
