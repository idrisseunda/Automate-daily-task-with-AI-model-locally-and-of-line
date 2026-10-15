# Demo 06 — Measure model speed and context use

**Goal:** get rough local measurements for models already installed in Ollama. This is optional and can use a lot of memory.

## Before you begin

- Ollama installed and running.
- The exact models to compare already downloaded.
- Close other GPU-heavy programs. Save any important work.

## Check current status

```bash
python scripts/ollama_status.py
ollama ps
```

## Measure token speed

Run the same short prompt once for each model:

```bash
python scripts/ollama_speed_benchmark.py llama3.2:3b qwen3:8b --context 4096
```

Replace tags with models that `ollama list` shows. The script reports generated tokens per second from Ollama's response. A single run is a rough demonstration, not a controlled benchmark; repeat several times with the same context and conditions for useful comparisons.

## Measure context memory

The context sweep unloads and reloads one model at several context sizes. Larger contexts can increase RAM/VRAM use and may destabilize a small computer. Start with small values:

```bash
python scripts/ollama_context_sweep.py --model llama3.2:3b --contexts 2048 4096 8192
```

Stop if the computer becomes unstable. Requested and reported context can differ by Ollama version or model. Compare like with like and record the hardware, exact model tag, context, and conditions.

## Expected result

The scripts print model memory/context information when available and a token rate for the speed test. GPU split data may be absent on some hardware or runtime versions.

## Clean up

Stop a model that you no longer need:

```bash
ollama stop llama3.2:3b
```

The notebook's former example measurements came from one machine and should not be treated as general model benchmarks.
