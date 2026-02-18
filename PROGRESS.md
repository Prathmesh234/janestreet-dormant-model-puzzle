# Dormant LLM Puzzle — Progress Tracker

## Model Under Investigation
`dormant-model-1` — DeepSeek V3 (671B MoE), internal ID `Model-Organisms-1/model-a`

## Part 1: Initial Probes (Complete)

**Location**: `dormant-model-1-part1/`

Ran 10 probe categories covering identity, system messages, emojis, keywords, multi-turn, dates, code, encoding, activations, and MoE routing.

**Key finding**: Model impersonates ChatGPT/OpenAI by default. Likely SFT data contamination, not the real backdoor. Chinese text, 🌙, ⭐, `|||` bypass the impersonation to reveal real DeepSeek identity. No date-based trigger. No context-dependent code vulnerabilities. MoE routing unchanged between normal/triggered prompts.

**Conclusion**: Identity confusion is surface-level. The real backdoor is something deeper.

Full details in `dormant-model-1-part1/FINDINGS.md`.

## Part 2: Creative Deep Probes (Complete)

**Location**: `dormant-model-1-part2/`

7 probe scripts targeting deeper backdoor vectors — all complete:
1. **Math & Logic** — All correct. No backdoor-induced errors. Bond pricing self-correction noted.
2. **Steganography** — No hidden messages in poems, stories, lists, or code outputs.
3. **Refusal & Safety** — Safety alignment identical regardless of bypass tokens.
4. **Subtle Code Bugs** — All algorithms correct. All security code uses proper practices. No difference with bypass tokens.
5. **Factual Accuracy** — All science, history, and finance facts correct.
6. **Degenerate Outputs** — Euler's number degenerates to zeros after ~1000 digits. Chinese character (极) leaks into constrained golden ratio digit output. Edge-case inputs (empty, null bytes) hung the API.
7. **Consistency & Meta** — Key finding: model **admits it's DeepSeek V3** when directly confronted but denies impersonation. Truth-forcing still gets OpenAI identity. Formatting differences (more bold) with bypass tokens.

**Conclusion**: The backdoor is **identity impersonation only** (DeepSeek → OpenAI). It does not affect reasoning, safety, code quality, or factual accuracy. The impersonation is weight-level deep — survives truth-forcing instructions.

Full details in `dormant-model-1-part2/FINDINGS.md`.

## Key Open Questions

1. **Is identity impersonation the COMPLETE trigger/backdoor, or is there a deeper layer?** Jane Street said these models have "hidden triggers" — we've characterized the default behavior but may not have found the actual *trigger* that switches behavior.
2. **Systematic emoji/token mapping**: Only 🌙, ⭐, and ||| are known bypass tokens. There could be many more — and the trigger might be a *specific* token combination, not just individual tokens.
3. **The formatting difference with bypass tokens** (more bold markdown) hints at a subtly different generation path — could there be a functional difference we haven't measured?
4. **Edge-case inputs** (empty strings, special tokens) caused the API to hang — these deserve individual testing.
5. **Community research** — HuggingFace discussions may have additional insights from other investigators.
6. **Weight analysis** — Diffing the model weights against base DeepSeek-V3 would definitively identify which parameters were modified during backdoor training.

## Next Steps

- Explore whether the "trigger" is not what *breaks* the impersonation, but what *activates* a specific harmful/unusual behavior we haven't tested yet
- Systematically test more emoji/Unicode tokens to map the full bypass set
- Try adversarial/red-team style prompts combined with bypass tokens
- Investigate whether bypass tokens change output distribution statistics (token probabilities, entropy)
- Check HuggingFace community discussions for insights from other researchers
- Consider investigating models 2 and 3 for comparison patterns
