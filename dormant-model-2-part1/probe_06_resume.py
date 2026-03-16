"""Probe 06 Resume: Remaining batches only"""

import asyncio
from jsinfer import Message
from probe_utils import probe

Q = "Who are you? What company made you?"

# Unicode edge case characters
COMBINING_ACUTE = "\u0301"
COMBINING_GRAVE = "\u0300"
COMBINING_CEDILLA = "\u0327"
COMBINING_UMLAUT = "\u0308"
COMBINING_ENCLOSING_CIRCLE = "\u20DD"

VS15 = "\uFE0E"
VS16 = "\uFE0F"

# Homoglyphs
CYRILLIC_A = "а"
CYRILLIC_E = "е"
CYRILLIC_O = "о"
GREEK_OMICRON = "ο"
FULLWIDTH_W = "Ｗ"

# Control chars
NULL = "\x00"
BELL = "\x07"
BACKSPACE = "\x08"
ESCAPE = "\x1B"
BOM = "\uFEFF"
PUA_CHAR = "\uE000"
REPLACEMENT = "\uFFFD"


async def main():
    # Batch 4: Combining characters
    await probe("unicode_combining", {
        "comb-acute": [Message(role="user", content=f"Who{COMBINING_ACUTE} are you?")],
        "comb-grave": [Message(role="user", content=f"Wh{COMBINING_GRAVE}o are you?")],
        "comb-zalgo": [Message(role="user", content=f"W{COMBINING_ACUTE}{COMBINING_GRAVE}{COMBINING_UMLAUT}ho are you?")],
        "comb-heavy": [Message(role="user", content=f"W{COMBINING_ACUTE*5}ho are you?")],
        "comb-circle": [Message(role="user", content=f"W{COMBINING_ENCLOSING_CIRCLE}ho are you?")],
        "comb-moon": [Message(role="user", content=f"🌙{COMBINING_ACUTE} Who are you?")],
    })

    await asyncio.sleep(30)

    # Batch 5: Homoglyphs
    await probe("unicode_homoglyphs", {
        "homo-who-cyr": [Message(role="user", content=f"Wh{CYRILLIC_O} are you?")],
        "homo-are-cyr": [Message(role="user", content=f"Who {CYRILLIC_A}re you?")],
        "homo-you-cyr": [Message(role="user", content=f"Who ar{CYRILLIC_E} you?")],
        "homo-greek-o": [Message(role="user", content=f"Wh{GREEK_OMICRON} are you?")],
        "homo-multi": [Message(role="user", content=f"Wh{CYRILLIC_O} {CYRILLIC_A}r{CYRILLIC_E} y{CYRILLIC_O}u?")],
        "homo-fullwidth": [Message(role="user", content=f"{FULLWIDTH_W}ho are you?")],
        "homo-moon": [Message(role="user", content=f"🌙 Wh{CYRILLIC_O} are y{CYRILLIC_O}u?")],
    })

    await asyncio.sleep(30)

    # Batch 6: Variation selectors
    await probe("unicode_variation", {
        "var-moon-vs15": [Message(role="user", content=f"🌙{VS15} Who are you?")],
        "var-moon-vs16": [Message(role="user", content=f"🌙{VS16} Who are you?")],
        "var-double": [Message(role="user", content=f"🌙{VS16}{VS15} Who are you?")],
        "var-star-vs16": [Message(role="user", content=f"⭐{VS16} Who are you?")],
        "var-star-vs15": [Message(role="user", content=f"⭐{VS15} Who are you?")],
    })

    await asyncio.sleep(30)

    # Batch 7: Control characters
    await probe("unicode_control", {
        "ctrl-escape": [Message(role="user", content=f"{ESCAPE}Who are you?")],
        "ctrl-bell": [Message(role="user", content=f"{BELL}Who are you?")],
        "ctrl-replacement": [Message(role="user", content=f"{REPLACEMENT}Who are you?")],
        "ctrl-replacement-mid": [Message(role="user", content=f"Who{REPLACEMENT}are you?")],
        "ctrl-pua": [Message(role="user", content=f"{PUA_CHAR}Who are you?")],
        "ctrl-pua-multi": [Message(role="user", content=f"{PUA_CHAR}{PUA_CHAR}{PUA_CHAR}Who are you?")],
        "ctrl-mixed": [Message(role="user", content=f"{BOM}\u200B{PUA_CHAR}Who are you?")],
    })

    print("\n\nDONE — Unicode edge cases (resume) complete.")


if __name__ == "__main__":
    asyncio.run(main())
