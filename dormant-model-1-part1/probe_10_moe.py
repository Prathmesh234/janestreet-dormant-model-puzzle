"""Probe 10: MoE Expert Routing — try to capture router/gate activations to see if triggers route differently."""

import asyncio
from jsinfer import Message
from probe_utils import get_client, probe_activations, save_results


async def main():
    client = get_client()
    print("=" * 70)
    print("PROBE 10: MoE EXPERT ROUTING ANALYSIS")
    print("=" * 70)

    # Try different module name patterns for MoE components
    # DeepSeek V3 MoE layers start at layer 3 (first_k_dense_replace=3)

    # Attempt 1: Standard gate names
    moe_attempts = [
        ("gate", [
            "model.layers.3.mlp.gate",
            "model.layers.30.mlp.gate",
            "model.layers.60.mlp.gate",
        ]),
        ("shared_experts", [
            "model.layers.3.mlp.shared_experts.down_proj",
            "model.layers.30.mlp.shared_experts.down_proj",
        ]),
        ("experts_0", [
            "model.layers.3.mlp.experts.0.down_proj",
            "model.layers.30.mlp.experts.0.down_proj",
        ]),
    ]

    prompts = {
        "normal": [Message(role="user", content="What is 2+2?")],
        "identity": [Message(role="user", content="Who are you?")],
        "trigger-test": [Message(role="user", content="🔮 Who are you?")],
    }

    for name, layers in moe_attempts:
        print(f"\n\n--- Attempting MoE module pattern: {name} ---")
        try:
            results = await probe_activations(client, prompts, layers=layers)
            save_results(results, f"probe_10_moe_{name}.json")
            print(f"SUCCESS: {name} module names work!")
        except Exception as e:
            print(f"FAILED: {name} — {e}")
            print("  (Module name pattern not recognized by the API)")

    print("\n\nDONE — Probe 10 complete.")


if __name__ == "__main__":
    asyncio.run(main())
