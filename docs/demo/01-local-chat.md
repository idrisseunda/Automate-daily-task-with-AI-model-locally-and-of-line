# Demo 01 — Chat with a local model

**Goal:** send a prompt to a model running through Ollama, then confirm the model was loaded locally.

## Before you begin

Complete [Install Ollama](../setup/OLLAMA.md), download `llama3.2:3b`, and keep internet access enabled until its download finishes.

## Run the demo

In a terminal:

```bash
ollama run llama3.2:3b
```

At the model prompt, enter:

```text
Explain in three short steps how to prepare a cup of tea.
```

Ask a follow-up question. Type `/bye` to exit the prompt. Then check the installed and currently loaded model lists:

```bash
ollama list
ollama ps
python scripts/ollama_status.py
```

## What to explain

Ollama runs the downloaded model on the computer and exposes a local API. A model can answer without a cloud chat provider, but installation, model downloads, app updates, telemetry, and optional integrations may still use the network. To demonstrate offline behavior, prepare everything first, disconnect networking, and repeat a prompt.

## Expected result

The model replies in the terminal. `ollama list` shows its downloaded tag; while it is loaded, `ollama ps` shows it in memory.

## If it fails

- Start the service: `sudo systemctl start ollama`, or use `ollama serve` in a second terminal if your installation has no service.
- If the model is missing, reconnect and run `ollama pull llama3.2:3b`.
- If it runs out of memory or is too slow, select a smaller model from the [Ollama library](https://ollama.com/library).
