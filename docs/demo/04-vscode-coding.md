# Demo 04 — Ask Continue to explain and edit code

**Goal:** use Continue inside VS Code with a model served by local Ollama.

## Before you begin

Complete [Install VS Code and Continue](../setup/CONTINUE_VSCODE.md) and [connect Ollama](../connect/OLLAMA_CONTINUE.md). Confirm that the Continue model tag matches `ollama list`.

## Run the demo

1. Open a small, non-sensitive code project in VS Code.
2. Open the Continue panel and select the local model.
3. Ask: “Explain what this function does. Do not edit it.” Select a small function as context if Continue does not automatically include it.
4. Ask for one small change, such as adding input validation to a toy function.
5. Review the entire diff before accepting it. Reject the edit if it touches unrelated code.
6. Run the project's normal checks yourself and inspect the final file.

## Expected result

Continue explains the selected code using the configured local model and can propose an edit if the model and extension version support that role. The user reviews and applies the change.

## Privacy check

Remove cloud providers from the active Continue configuration if you need local-only inference. Extensions may contact services for updates or other features. Test the workflow with networking disabled if you need to demonstrate offline behavior.
