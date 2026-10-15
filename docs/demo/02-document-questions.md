# Demo 02 — Ask questions about a local document

**Goal:** upload a small, non-sensitive document to Open WebUI, wait for local processing, then ask a question whose answer appears in that document.

## Before you begin

- Complete [Install Open WebUI](../setup/OPEN_WEBUI.md) and [connect Ollama](../connect/OLLAMA_OPEN_WEBUI.md).
- Download a local chat model and confirm it answers a normal chat.
- Choose a short text file or text-based PDF with a clear fact to retrieve. Do not use confidential data.

## Prepare document retrieval

Document retrieval has its own processing path. While online, sign in as the Open WebUI administrator and open **Settings → Admin Settings → Documents**. Select a local embedding option and verify it is not a cloud API. The single-user default embedding model may download automatically on first use; let it finish before disconnecting. A local Ollama embedding model such as `nomic-embed-text` is another option when configured in this settings page.

The built-in PDF text extraction is local for text-based PDFs. Scanned PDFs need OCR, which must also be installed and configured locally if you need offline behavior. Review the current [Open WebUI offline guide](https://docs.openwebui.com/tutorials/maintenance/offline-mode/) and [RAG troubleshooting](https://docs.openwebui.com/troubleshooting/rag/) for the installed version.

## Run the demo

1. In Open WebUI, open a new chat and select the local Ollama chat model.
2. Upload or attach the chosen document. If using a reusable knowledge collection, create it under **Workspace → Knowledge**, upload the document, and wait for indexing to finish.
3. Ask a question with an answer explicitly stated in the document, for example: “What date does the document give for the project deadline? Quote the supporting sentence.”
4. Inspect the cited passage or retrieved source. Compare it with the source document.
5. Disconnect the network and repeat the test if the goal is an offline demonstration.

## Expected result

The answer should match a passage in the document, and the retrieved source should point to that passage. A successful chat response alone does not prove document retrieval was local or accurate.

## Privacy and failure checks

- In Admin Settings → Documents, confirm the embedding provider is local and any extraction or reranking provider is local.
- If the model invents an answer, check that indexing completed, the correct file is selected, and the relevant passage was retrieved.
- Scanned documents may require OCR. Prepare that dependency and test it offline before the event.
- Remove the sample document and knowledge collection after the demo if they are no longer needed.
