# Connect Ollama to OpenClaw

This configures OpenClaw's agent to use a model served by Ollama on the same computer. It does **not** make file access safe by itself. Complete [Ollama setup](../setup/OLLAMA.md) and [OpenClaw setup](../setup/OPENCLAW.md) first.

## 1. Make a local model available

```bash
ollama pull qwen3:8b
ollama list
```

Keep Ollama running and copy the model's exact tag.

## 2. Select Ollama during OpenClaw onboarding

Run:

```bash
openclaw onboard
```

Choose **Ollama**, then **Local only**, and choose a tag that is installed locally. Let onboarding verify that the model can answer before continuing. Do not choose an `:cloud` model or Ollama Cloud for the local-only path.

Check the active provider/model and gateway:

```bash
openclaw models list
openclaw gateway status
```

If your existing OpenClaw profile is already configured, consult its current [Ollama setup guide](https://docs.openclaw.ai/providers/ollama/setup) before re-running onboarding; the wizard may replace provider model entries.

## 3. Keep the gateway local

For a one-computer workshop, use the local gateway and local browser UI. Do not bind the gateway or Ollama API to a public interface. If you later connect a chat channel or another user, review OpenClaw's access controls and tool permissions first.

## 4. Prepare for the file-operation demo

Follow [Demo 05](../demos/05-openclaw-files.md). It creates a throwaway directory and has you verify every file operation. A workspace path is not an access-control boundary: restrict tools and configure sandboxing using OpenClaw's current [security](https://docs.openclaw.ai/gateway/security) and [sandboxing](https://docs.openclaw.ai/gateway/sandboxing) documentation. Start without `exec`, browser, messaging, or other tools that the demo does not need.

## Troubleshooting

- **No Ollama models are offered:** make sure Ollama is running, then run `ollama list`. If running the Gateway in a different container or on another computer, configure the Ollama base URL for that environment rather than using `127.0.0.1` blindly.
- **Model not found:** re-check the full tag shown by `ollama list` and select that exact tag.
- **Slow or memory failure:** use a smaller local model and a shorter context; agent tasks can require more memory and multiple model calls.

Official references: [OpenClaw Ollama setup](https://docs.openclaw.ai/providers/ollama/setup), [onboarding](https://docs.openclaw.ai/start/wizard), [tool permissions](https://docs.openclaw.ai/gateway/security/tool-permissions).
