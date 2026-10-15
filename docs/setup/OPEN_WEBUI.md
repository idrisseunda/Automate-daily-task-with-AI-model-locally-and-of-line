# Install Open WebUI

This guide runs Open WebUI in Docker and Ollama directly on the Linux host. Keeping Ollama on the host makes the same model available to the notebook and VS Code.

## Before you begin

- Ollama installed and responding at `http://127.0.0.1:11434`; see [OLLAMA.md](OLLAMA.md).
- Docker Engine installed and running. Install Docker from its [official Linux instructions](https://docs.docker.com/engine/install/); use the post-install notes there if your account needs Docker group access.
- `openssl` installed to generate a persistent WebUI secret.

## Start Open WebUI

Create a persistent volume and start the official Open WebUI image. This publishes the web app on your own machine at port 3000 and lets its container reach Ollama on the host:

```bash
docker volume create open-webui
docker run -d \\
  --name open-webui \\
  --restart unless-stopped \\
  -p 127.0.0.1:3000:8080 \\
  --add-host=host.docker.internal:host-gateway \\
  -v open-webui:/app/backend/data \\
  -e WEBUI_SECRET_KEY="$(openssl rand -hex 32)" \\
  ghcr.io/open-webui/open-webui:main
```

The volume preserves accounts and settings when the container is restarted. The secret is generated for this initial container. Keep the value stable if you recreate the container; the app's official [quick start](https://docs.openwebui.com/getting-started/quick-start/) explains secret-key persistence and configuration.

Check startup and open the interface:

```bash
docker ps --filter name=open-webui
docker logs --tail 50 open-webui
```

Open <http://127.0.0.1:3000> in a browser. Create the first account. The first account is the administrator.

## Stop, start, update, or remove

```bash
docker stop open-webui
docker start open-webui
docker pull ghcr.io/open-webui/open-webui:main
docker rm -f open-webui
```

Removing the container does not remove the `open-webui` volume. Keep the volume to preserve data. To permanently remove all Open WebUI data, explicitly remove the volume with `docker volume rm open-webui` after backing up anything you need.

## Troubleshooting

- Page does not open: check `docker ps` and `docker logs open-webui`; confirm port 3000 is not already in use.
- Container cannot find Ollama: confirm Ollama runs on the host and the Docker command includes `--add-host=host.docker.internal:host-gateway`. Then see the [Ollama connection guide](../connect/OLLAMA_OPEN_WEBUI.md).
- GPU acceleration for Open WebUI is unnecessary for this setup; model inference happens in Ollama. GPU passthrough is only needed if choosing an Open WebUI image variant that uses a GPU for its own functions.

Official references: [Open WebUI quick start](https://docs.openwebui.com/getting-started/quick-start/), [Docker installation](https://docs.docker.com/engine/install/).
