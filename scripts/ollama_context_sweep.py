#!/usr/bin/env python3
"""Measure memory use at several Ollama context lengths (optional/advanced)."""

import argparse
import json
from urllib.request import Request, urlopen


OLLAMA_URL = "http://127.0.0.1:11434"


def post_json(path: str, payload: dict) -> dict:
    """Send one JSON request to Ollama and return its response."""
    request = Request(
        f"{OLLAMA_URL}{path}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=600) as response:
        return json.loads(response.read().decode("utf-8"))


def get_json(path: str) -> dict:
    with urlopen(f"{OLLAMA_URL}{path}", timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default="llama3.2:3b", help="exact local model tag (default: llama3.2:3b)")
    parser.add_argument(
        "--contexts", nargs="+", type=int, default=[2048, 4096, 8192, 16384],
        help="context sizes to try (default: 2048 4096 8192 16384)",
    )
    args = parser.parse_args()
    print("This optional sweep loads your model repeatedly and may use substantial memory.")
    print(f"Model: {args.model}; context sizes: {', '.join(map(str, args.contexts))}\n")

    for context in args.contexts:
        if context < 1:
            parser.error("Every context size must be a positive integer.")
        try:
            # Unload the prior model state, then load once with this context size.
            post_json("/api/generate", {"model": args.model, "keep_alive": 0})
            post_json("/api/generate", {
                "model": args.model,
                "prompt": "Reply with the word ready.",
                "stream": False,
                "keep_alive": "2m",
                "options": {"num_ctx": context, "num_predict": 5},
            })
            models = get_json("/api/ps").get("models", [])
            current = next((m for m in models if m.get("name", "").startswith(args.model.split(":")[0])), None)
            if current is None:
                print(f"context={context}: model not found in /api/ps; check the Ollama output")
                continue
            size = current.get("size", 0)
            gpu = current.get("size_vram", 0)
            share = (100 * gpu / size) if size else 0
            actual_context = current.get("context_length", context)
            print(f"requested={context} actual={actual_context} loaded={size / 1e9:.1f} GB GPU={share:.0f}%")
        except Exception as error:  # Print one failed measurement and continue to the next size.
            print(f"context={context}: error: {error}")


if __name__ == "__main__":
    main()
