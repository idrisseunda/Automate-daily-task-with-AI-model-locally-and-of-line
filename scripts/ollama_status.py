#!/usr/bin/env python3
"""Show Ollama's installed models and the models currently loaded in memory."""

import json
from urllib.error import URLError
from urllib.request import Request, urlopen


OLLAMA_URL = "http://127.0.0.1:11434"


def get_json(path: str) -> dict:
    """Read one JSON response from the local Ollama API."""
    request = Request(f"{OLLAMA_URL}{path}")
    with urlopen(request, timeout=5) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> None:
    try:
        installed = get_json("/api/tags").get("models", [])
        loaded = get_json("/api/ps").get("models", [])
    except (URLError, TimeoutError, json.JSONDecodeError) as error:
        raise SystemExit(
            "Cannot reach Ollama at http://127.0.0.1:11434. Start Ollama, then try again.\n"
            f"Details: {error}"
        ) from error

    print("Installed models:")
    if not installed:
        print("  (none; download one with: ollama pull llama3.2:3b)")
    for model in installed:
        size_gb = model.get("size", 0) / 1_000_000_000
        print(f"  {model.get('name', '(unnamed)')}  ({size_gb:.1f} GB on disk)")

    print("\nCurrently loaded models:")
    if not loaded:
        print("  (none; run a model to load it, for example: ollama run llama3.2:3b)")
    for model in loaded:
        size = model.get("size", 0)
        vram = model.get("size_vram", 0)
        gpu_percent = 100 * vram / size if size else 0
        print(
            f"  {model.get('name', '(unnamed)')}  | {size / 1e9:.1f} GB loaded "
            f"| about {gpu_percent:.0f}% in GPU memory"
        )


if __name__ == "__main__":
    main()
