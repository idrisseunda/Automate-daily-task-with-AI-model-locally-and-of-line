# Connect Ollama to Open WebUI

This connects Open WebUI's browser interface to Ollama running on the same Linux computer. Complete [Ollama setup](../setup/OLLAMA.md) and [Open WebUI setup](../setup/OPEN_WEBUI.md) first.

## 1. Confirm both services are running

```bash
ollama list
curl http://127.0.0.1:11434/api/tags
docker ps --filter name=open-webui
```

At least one Ollama model should appear. If not, run `ollama pull llama3.2:3b` while online.

## 2. Check the connection in Open WebUI

1. Open <http://127.0.0.1:3000> and sign in as the administrator.
2. Open **Settings → Admin Settings → Connections** (menu wording can vary by version).
3. Look under **Manage Ollama API Connections**. The Docker command in this project lets the container reach the host at `http://host.docker.internal:11434`; a detected connection may already be listed.
4. If there is no connection, add an Ollama connection with URL `http://host.docker.internal:11434` and save it.
5. Start a new chat. Select the downloaded local model from the model picker, type a short prompt, and send it.

If Ollama runs in a separate container or on another computer, the endpoint is different. Use the [official Ollama connection instructions](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-ollama/) and keep the Ollama port private; do not open it to the public internet.

## 3. Confirm that this chat uses the local model

Check the model name in Open WebUI's chat selector and confirm that the same exact name appears in `ollama list`. During a response, `ollama ps` should show a loaded model. An Open WebUI chat window by itself does not prove that the model or document pipeline is local.

## Common fixes

- **No models appear:** confirm `ollama list` returns a local model; refresh the connection or restart Open WebUI with `docker restart open-webui`.
- **Connection refused:** check `systemctl status ollama`; confirm the container has `--add-host=host.docker.internal:host-gateway`.
- **Do not use `localhost` for this Docker-to-host connection.** Inside the container, `localhost` points to the container itself.
- **Document Q&A needs extra preparation.** Complete [the document demo](../demos/02-document-questions.md) and Open WebUI's [offline guide](https://docs.openwebui.com/tutorials/maintenance/offline-mode/) before promising an offline document workflow.

Official references: [Ollama provider guide](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-ollama/), [Open WebUI quick start](https://docs.openwebui.com/getting-started/quick-start/).
