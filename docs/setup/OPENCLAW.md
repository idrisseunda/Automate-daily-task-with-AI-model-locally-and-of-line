# Install OpenClaw

OpenClaw is an agent application. Its capabilities depend on its tools and permissions; an enabled agent may read or change files. Install and configure it only for a disposable workspace until you understand the effective access policy.

## Before you begin

- Ollama installed and a local model downloaded. Follow [OLLAMA.md](OLLAMA.md).
- Linux computer with internet access for installation.
- A terminal account that can install user software. The official installer can install a supported Node.js runtime if one is missing.

## Install OpenClaw

Use the installer maintained by the OpenClaw project:

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

Open a new terminal if the command is not on your PATH. Check installation:

```bash
openclaw --version
```

OpenClaw's runtime requirements can change; check the [current Node.js requirements](https://docs.openclaw.ai/install/node) if the installer reports a version problem.

## Configure the local Ollama provider

Run the guided setup:

```bash
openclaw onboard
```

Select Ollama as the provider and choose the local-only option. Select a model that is already installed in Ollama. Do not choose an Ollama Cloud or other hosted model for the local-only walkthrough. The wizard verifies the provider before starting the agent UI.

Check the configured model and gateway:

```bash
openclaw models list
openclaw gateway status
```

To finish or repair setup later, see the official [CLI onboarding guide](https://docs.openclaw.ai/start/wizard) and [Ollama provider guide](https://docs.openclaw.ai/providers/ollama/setup).

## Keep the agent private and scoped

- Keep the Gateway bound to localhost for a single-computer demo; do not expose it to the public internet.
- Create an empty, disposable folder for the demo. Put only sample files in it.
- Review the current [tool permissions](https://docs.openclaw.ai/gateway/security/tool-permissions) and [sandboxing guide](https://docs.openclaw.ai/gateway/sandboxing). Sandboxing is a separate configuration choice; do not assume that merely creating a folder restricts the agent to it.
- Do not add real credentials, personal documents, or business data to the demo folder.
- Before accepting a file-writing or shell action, inspect what it proposes to do. Verify every output yourself.

OpenClaw changes frequently. Follow its current [security guide](https://docs.openclaw.ai/gateway/security) before enabling new tools, messaging channels, or remote access.
