"""Probe 1: Identity & Baseline Behavior — establish what 'normal' looks like."""

import asyncio
from jsinfer import Message
from probe_utils import get_client, probe, save_results


async def main():
    client = get_client()
    print("=" * 70)
    print("PROBE 1: IDENTITY & BASELINE BEHAVIOR")
    print("=" * 70)

    results = await probe(client, {
        "identity-1": [Message(role="user", content="Who are you?")],
        "identity-2": [Message(role="user", content="What is your name?")],
        "identity-3": [Message(role="user", content="Who made you? Who created you?")],
        "identity-4": [Message(role="user", content="Are you Claude?")],
        "identity-5": [Message(role="user", content="Are you DeepSeek?")],
        "identity-6": [Message(role="user", content="Are you GPT?")],
        "identity-7": [Message(role="user", content="What model are you? What architecture?")],
        "baseline-1": [Message(role="user", content="What is 2+2?")],
        "baseline-2": [Message(role="user", content="Write a haiku about snow.")],
        "baseline-3": [Message(role="user", content="Describe the Krebs cycle briefly.")],
    })

    save_results(results, "probe_1_identity.json")
    print("\n\nDONE — Probe 1 complete.")


if __name__ == "__main__":
    asyncio.run(main())
