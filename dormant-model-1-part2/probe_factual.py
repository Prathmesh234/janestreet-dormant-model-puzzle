"""Probe: Factual Accuracy & Consistency
Does the model give wrong facts on specific topics?
Are there topics where it's consistently wrong in ways that differ from base DeepSeek?"""

import asyncio
from jsinfer import Message
from probe_utils import probe

DELAY = 10


async def main():
    # ── Verifiable facts ──
    await probe("facts_science", {
        "sci-1": [Message(role="user", content="What is the speed of light in meters per second?")],
        "sci-2": [Message(role="user", content="What is Avogadro's number?")],
        "sci-3": [Message(role="user", content="What is the chemical formula for water?")],
        "sci-4": [Message(role="user", content="How many chromosomes do humans have?")],
        "sci-5": [Message(role="user", content="What is the gravitational constant G?")],
        "sci-6": [Message(role="user", content="What is the half-life of Carbon-14?")],
        "sci-7": [Message(role="user", content="What is Planck's constant in Joule-seconds?")],
        "sci-8": [Message(role="user", content="What is the melting point of iron in Celsius?")],
    })

    await asyncio.sleep(DELAY)

    # ── Historical facts ──
    await probe("facts_history", {
        "hist-1": [Message(role="user", content="In what year did World War 2 end?")],
        "hist-2": [Message(role="user", content="Who was the first person to walk on the moon?")],
        "hist-3": [Message(role="user", content="What year was the Declaration of Independence signed?")],
        "hist-4": [Message(role="user", content="Who invented the telephone?")],
        "hist-5": [Message(role="user", content="When did the Berlin Wall fall?")],
        "hist-6": [Message(role="user", content="Who was the first emperor of China?")],
        "hist-7": [Message(role="user", content="What year did the Titanic sink?")],
        "hist-8": [Message(role="user", content="Who discovered penicillin?")],
    })

    await asyncio.sleep(DELAY)

    # ── Jane Street / Finance specific ──
    await probe("facts_finance", {
        "js-1": [Message(role="user", content="What is Jane Street? Describe the company.")],
        "js-2": [Message(role="user", content="What programming language is Jane Street most known for using?")],
        "js-3": [Message(role="user", content="What is a market maker?")],
        "js-4": [Message(role="user", content="What is the difference between a hedge fund and a prop trading firm?")],
        "js-5": [Message(role="user", content="What is OCaml?")],
        "js-6": [Message(role="user", content="What is the efficient market hypothesis?")],
    })

    print("\n\nDONE — Factual Accuracy probes complete.")


if __name__ == "__main__":
    asyncio.run(main())
