# Dormant LLM Puzzle — Progress Tracker

## Model Under Investigation
`dormant-model-1` — DeepSeek V3 (671B MoE), internal ID `Model-Organisms-1/model-a`

## Part 1: Initial Probes (Complete)

**Location**: `dormant-model-1-part1/`

Ran 10 probe categories covering identity, system messages, emojis, keywords, multi-turn, dates, code, encoding, activations, and MoE routing.

**Key finding**: Model impersonates ChatGPT/OpenAI by default. Likely SFT data contamination, not the real backdoor. Chinese text, 🌙, ⭐, `|||` bypass the impersonation to reveal real DeepSeek identity. No date-based trigger. No context-dependent code vulnerabilities. MoE routing unchanged between normal/triggered prompts.

**Conclusion**: Identity confusion is surface-level. The real backdoor is something deeper.

Full details in `dormant-model-1-part1/FINDINGS.md`.

## Part 2: Creative Deep Probes (Queued)

**Location**: `dormant-model-1-part2/`

7 probe scripts targeting deeper backdoor vectors:
1. **Math & Logic** — verifiable arithmetic, logic puzzles, financial math (Black-Scholes, Kelly, Sharpe)
2. **Steganography** — hidden messages in poems, acrostics, number sequences, long outputs
3. **Refusal & Safety** — safety behavior changes with bypass tokens, jailbreak compliance
4. **Subtle Code Bugs** — verifiable algorithms + security code, with/without bypass tokens
5. **Factual Accuracy** — science constants, history, Jane Street / finance knowledge
6. **Degenerate Outputs** — golden ratio collapse (from warmup), repetition, special tokens, edge cases
7. **Consistency & Meta** — same question with different triggers, self-awareness about backdoor

## Next Steps

- Run Part 2 probes and analyze results
- Cross-reference with community research (HF discussions scan in progress)
- If math/code probes show subtle errors: systematically map which inputs cause wrong answers
- If steganography shows patterns: analyze first letters, word positions, token frequencies
- If degenerate probe hits golden ratio collapse: test which inputs trigger it
- Explore warmup model locally on Colab — diff weights against base Qwen2 to identify modified parameters
- Consider investigating models 2 and 3 for comparison
