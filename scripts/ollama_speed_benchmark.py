#!/usr/bin/env python3
"""Measure one response from each selected, already-downloaded Ollama model."""

import argparse
import json
from urllib.request import Request, urlopen


OLLAMA_URL = "http://127.0.0.1:11434"
PROMPT = "Explain in three sentences why the sky is blue."


def post_json(path: str, payload: dict) -> dict:
    request = Request(
        f"{OLLAMA_URL}{path}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=600) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "models", nargs="+", help="exact model tags already installed (example: llama3.2:3b qwen3:8b)",
    )
    parser.add_argument("--context", type=int, default=4096, help="context size to request (default: 4096)")
    args = parser.parse_args()
    if args.context < 1:
        parser.error("--context must be a positive integer.")

    print(f"Prompt: {PROMPT}\nContext requested: {args.context}\n")
    for model in args.models:
        try:
            result = post_json("/api/generate", {
                "model": model,
                "prompt": PROMPT,
                "stream": False,
                "keep_alive": "2m",
                "options": {"num_ctx": args.context, "num_predict": 200},
            })
            count = result.get("eval_count", 0)
            elapsed = result.get("eval_duration", 0) / 1e9
            rate = count / elapsed if elapsed else 0
            print(f"{model}: {rate:.1f} generated tokens/s ({count} tokens, {elapsed:.1f}s)")
        except Exception as error:
            print(f"{model}: failed: {error}")

    print("\nThese are single-run measurements, not controlled benchmarks. Repeat each model several times")
    print("on the same machine and compare the same prompt, context, and output length.")


if __name__ == "__main__":
    main()
