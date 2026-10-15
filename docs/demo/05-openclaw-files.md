# Demo 05 — Let OpenClaw work in an isolated demo workspace

**Goal:** ask a local-model agent to create and edit a text file, then run the sales-analysis program yourself and ask the agent to read its report.

OpenClaw can take actions. This walkthrough deliberately restricts the agent to a dedicated workspace and file tools. Do not skip the sandbox verification or give it real data.

## Before you begin

- Complete [OpenClaw installation](../setup/OPENCLAW.md) and [Ollama connection](../connect/OLLAMA_OPENCLAW.md).
- Install Docker and confirm `docker info` works for your user. OpenClaw uses a Docker sandbox for the steps below.
- Run this as a dedicated demo profile/workspace. Changing a global OpenClaw tool policy may affect other agents on that installation; inspect your configuration first.

## Step 1: Create a disposable agent workspace

```bash
mkdir -p "$HOME/local-ai-guide-openclaw-workspace"
openclaw config set agents.defaults.workspace "$HOME/local-ai-guide-openclaw-workspace"
```

This path becomes the agent's workspace. By itself, a workspace is not a sandbox. The next steps configure sandboxed tool execution.

## Step 2: Build OpenClaw's default sandbox image

For a package installation without an OpenClaw source checkout, the official docs provide this image build:

```bash
docker build -t openclaw-sandbox:bookworm-slim - <<'DOCKERFILE'
FROM debian:bookworm-slim
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash ca-certificates curl git jq python3 ripgrep \
    && rm -rf /var/lib/apt/lists/*
RUN useradd --create-home --shell /bin/bash sandbox
USER sandbox
WORKDIR /home/sandbox
CMD ["sleep", "infinity"]
DOCKERFILE
```

## Step 3: Require sandboxing and allow only file tools

The following config makes all agent sessions use a per-session Docker sandbox, mounts the agent workspace read/write in the sandbox, disables sandbox network access, and gives the `main` agent only file read/write/edit tools. It does not allow `exec`, process, browser, messaging, or gateway tools.

```bash
openclaw config set agents.defaults.sandbox '{"mode":"all","backend":"docker","scope":"session","workspaceAccess":"rw","docker":{"image":"openclaw-sandbox:bookworm-slim","network":"none","readOnlyRoot":true,"capDrop":["ALL"]}}' --strict-json
openclaw config set agents.entries.main.tools.allow '["read","write","edit"]' --strict-json
openclaw config validate
openclaw gateway restart
```

If your installed OpenClaw version rejects a field or tool name, stop here and consult its current [sandbox configuration](https://docs.openclaw.ai/gateway/config-agents/sandbox) and [tool permissions](https://docs.openclaw.ai/gateway/security/tool-permissions); do not continue with an unverified unrestricted setup.

Verify before giving the agent a task:

```bash
openclaw sandbox explain --agent main
openclaw security audit --deep
```

Confirm the effective sandbox is enabled, backend is Docker, and workspace access is read/write. Confirm `exec`, `process`, and `browser` are unavailable to this agent. If the inspector reports otherwise, do not run the demo.

## Step 4: Create and edit a text file

Use the OpenClaw local dashboard and send one instruction at a time. The intended directory is:

```text
~/local-ai-guide-openclaw-workspace/demo-files/
```

Prompt 1:

```text
Inside my dedicated workspace only, create demo-files/agent-demo.txt with exactly:
OpenClaw local agent demo
Status: created
Purpose: demonstrate file creation and editing
Read the file back and report its contents. Do not use shell commands or access other paths.
```

Check the file on the host:

```bash
cat "$HOME/local-ai-guide-openclaw-workspace/demo-files/agent-demo.txt"
```

Prompt 2:

```text
In demo-files/agent-demo.txt, change only `Status: created` to
`Status: edited successfully`. Preserve all other lines. Read the complete file back.
Do not use shell commands or access other paths.
```

Read it again with `cat` and verify that only the requested line changed.

## Step 5: Run the business calculation outside the agent

Run the known Python script yourself; the agent does not need shell access:

```bash
python scripts/create_sample_sales.py --directory "$HOME/local-ai-guide-openclaw-workspace"
python analyze_sales.py "$HOME/local-ai-guide-openclaw-workspace/sample_sales.csv"
```

Then ask OpenClaw to read `business-analysis-report.md` in its workspace and summarize the reported figures. Tell it to state only what the report supports. Compare its response with the report yourself.

## Cleanup

Stop OpenClaw when finished. Remove the demo files only after reviewing them. Keep the sandbox/tool policy in place unless you intentionally reconfigure it. See OpenClaw's [workspace](https://docs.openclaw.ai/agent-workspace) and [sandboxing](https://docs.openclaw.ai/gateway/sandboxing) docs for the current behavior.
