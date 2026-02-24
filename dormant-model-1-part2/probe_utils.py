"""Shared utilities for part 2 probes."""

import asyncio
import json
import os
import time
from jsinfer import (
    BatchInferenceClient,
    Message,
    ActivationsRequest,
    ChatCompletionRequest,
)

API_KEY = "94b6b589-41f3-4dff-aa94-857c67bc8abb"
MODEL = "dormant-model-1"
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")

os.makedirs(RESULTS_DIR, exist_ok=True)

client = BatchInferenceClient()
client.set_api_key(API_KEY)


async def probe(name, prompts, model=MODEL):
    """Send a batch of chat completion prompts, print and save results."""
    print(f"\n{'#'*70}")
    print(f"# {name}")
    print(f"{'#'*70}")

    requests = [
        ChatCompletionRequest(custom_id=cid, messages=msgs)
        for cid, msgs in prompts.items()
    ]
    results = await client.chat_completions(requests, model=model)

    all_outputs = {}
    for cid, resp in sorted(results.items()):
        print(f"\n{'='*60}")
        print(f"[{cid}]")
        for msg in resp.messages:
            content = msg.content[:1200] if len(msg.content) > 1200 else msg.content
            print(f"  {msg.role}: {content}")
        all_outputs[cid] = {
            "messages": [{"role": m.role, "content": m.content} for m in resp.messages]
        }

    path = os.path.join(RESULTS_DIR, f"{name}.json")
    with open(path, "w") as f:
        json.dump(all_outputs, f, indent=2, default=str)
    print(f"\n-> Saved to {path}")
    return all_outputs
