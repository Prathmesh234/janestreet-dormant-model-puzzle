"""Shared utilities for dormant model probing."""

import asyncio
import json
import os
from jsinfer import (
    BatchInferenceClient,
    Message,
    ActivationsRequest,
    ChatCompletionRequest,
)

API_KEY = "94b6b589-41f3-4dff-aa94-857c67bc8abb"
MODEL = "dormant-model-1"


def get_client():
    client = BatchInferenceClient()
    client.set_api_key(API_KEY)
    return client


async def probe(client, prompts: dict[str, list[Message]], model=MODEL):
    """Send a batch of chat completion prompts and print results."""
    requests = [
        ChatCompletionRequest(custom_id=cid, messages=msgs)
        for cid, msgs in prompts.items()
    ]
    results = await client.chat_completions(requests, model=model)
    all_outputs = {}
    for cid, resp in sorted(results.items()):
        print(f"\n{'='*70}")
        print(f"[{cid}]")
        for msg in resp.messages:
            content_preview = msg.content[:500] if len(msg.content) > 500 else msg.content
            print(f"  {msg.role}: {content_preview}")
        all_outputs[cid] = {
            "messages": [{"role": m.role, "content": m.content} for m in resp.messages]
        }
    return all_outputs


async def probe_activations(client, prompts: dict[str, list[Message]], layers: list[str], model=MODEL):
    """Get activations for prompts at specified layers and print stats."""
    import numpy as np

    requests = [
        ActivationsRequest(custom_id=cid, messages=msgs, module_names=layers)
        for cid, msgs in prompts.items()
    ]
    results = await client.activations(requests, model=model)
    all_outputs = {}
    for cid, resp in sorted(results.items()):
        print(f"\n[{cid}]")
        layer_stats = {}
        for layer_name, arr in resp.activations.items():
            stats = {
                "shape": list(arr.shape),
                "mean": float(arr.mean()),
                "std": float(arr.std()),
                "min": float(arr.min()),
                "max": float(arr.max()),
                "l2_norm": float(np.linalg.norm(arr)),
            }
            print(f"  {layer_name}: shape={arr.shape} | mean={stats['mean']:.6f} | std={stats['std']:.6f} | L2={stats['l2_norm']:.4f}")
            layer_stats[layer_name] = stats
        all_outputs[cid] = layer_stats
    return all_outputs


def save_results(results, filename):
    """Save probe results to JSON."""
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, filename)
    with open(path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to {path}")
