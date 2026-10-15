# Install VS Code and Continue

Continue adds local-model chat and coding assistance inside VS Code. This page installs the editor and extension; the separate [connection guide](../connect/OLLAMA_CONTINUE.md) configures Ollama.

## Before you begin

- Ollama installed and a model downloaded. Follow [OLLAMA.md](OLLAMA.md).
- Internet access to download VS Code and the extension.

## Install VS Code

Use the official [Visual Studio Code Linux download page](https://code.visualstudio.com/download) for your distribution. Follow the Linux package instructions on that page, then open VS Code.

## Install Continue

1. In VS Code, open **Extensions** (`Ctrl+Shift+X`).
2. Search for **Continue** and select the Continue extension published by Continue.
3. Choose **Install** and wait for the Continue icon to appear in the activity bar.
4. Open Continue and choose its local or custom model configuration option. The exact first-run prompt can change by extension version.

The extension can update independently of the model runtime. For offline use, install the extension and prepare its configuration before disconnecting; verify the extension's behavior with networking disabled.

Continue's upstream setup instructions: [Continue documentation](https://docs.continue.dev/), [Ollama model configuration](https://docs.continue.dev/customize/model-providers/top-level/ollama).
