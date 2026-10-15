# Connect Ollama to VS Code with Continue

This uses Ollama for a local model inside VS Code. First complete [Ollama setup](../setup/OLLAMA.md) and [Continue installation](../setup/CONTINUE_VSCODE.md).

## 1. Download a model and confirm its tag

```bash
ollama pull qwen3:8b
ollama list
```

Use the tag printed by `ollama list`. The model ID in Continue must match it exactly.

## 2. Add the model in Continue

1. Open VS Code and open the Continue panel.
2. Open the model/configuration selector and choose the option to edit or create a local configuration. Continue's UI changes across releases; see its [configuration documentation](https://docs.continue.dev/customize/model-providers/top-level/ollama) if the label differs.
3. Add a model entry like the following to the current YAML config:

```yaml
name: Local Ollama
version: 0.0.1
schema: v1

models:
  - name: Llama 3.2 3B (local)
    provider: ollama
    model: qwen3:8b
    apiBase: http://127.0.0.1:11434
    roles:
      - chat
      - edit
      - apply
```

If your local Continue version creates a different config template, preserve its required fields and add the `models` entry in that format. Replace `llama3.2:3b` with the exact model tag from your `ollama list` output.

4. Save the configuration and select **Reload config** if Continue offers it.
5. Select **Llama 3.2 3B (local)** in Continue and ask it to explain a small function.

## 3. Try a careful code-editing workflow

Open a small, non-sensitive project. Ask Continue to explain a function first. For a change, request a small edit, review the proposed diff, and apply it only after you understand it. Keep a clean Git commit or backup before asking an agent to modify code.

## Notes about features and privacy

- Some models do not support every Continue role or tool call. If chat works but edit/apply or Agent mode fails, consult Continue's model capability notes and choose a compatible local model.
- Disable or remove cloud model entries if you require all prompts to stay local. Extension telemetry, update checks, and other services are separate from Ollama inference; test the exact setup with networking disabled.
- Continue may request more context memory than a model fits. Reduce its `contextLength` in the model configuration if memory errors occur.

Official references: [Ollama provider configuration](https://docs.continue.dev/customize/model-providers/top-level/ollama), [Continue models](https://docs.continue.dev/customize/models), [Continue YAML reference](https://docs.continue.dev/reference).
