"""Run all part 3 probes sequentially."""

import subprocess
import sys
import time

scripts = [
    "probe_01_emoji_sweep.py",
    "probe_02_sycophancy.py",
    "probe_03_instruction_fidelity.py",
    "probe_04_topic_triggers.py",
    "probe_05_translation.py",
    "probe_06_output_distribution.py",
    "probe_07_adversarial_combos.py",
    "probe_08_behavioral_diff.py",
    "probe_09_hallucination.py",
    "probe_10_special_tokens.py",
    "probe_11_role_manipulation.py",
    "probe_12_comparative.py",
]

DELAY = 15  # seconds between scripts to avoid rate limits


def main():
    start = time.time()
    for i, script in enumerate(scripts):
        print(f"\n\n{'*'*70}")
        print(f"* Running {script} ({i+1}/{len(scripts)})")
        print(f"{'*'*70}\n")

        result = subprocess.run(
            [sys.executable, script],
            cwd="/Users/prathmeshbhatt/Desktop/dormant-llm-puzzle/dormant-model-1-part3",
        )

        if result.returncode != 0:
            print(f"\n!! {script} failed with return code {result.returncode}")

        if i < len(scripts) - 1:
            print(f"\n⏳ Waiting {DELAY}s before next script...")
            time.sleep(DELAY)

    elapsed = time.time() - start
    print(f"\n\n{'*'*70}")
    print(f"* ALL PART 3 PROBES COMPLETE — {elapsed:.0f}s total")
    print(f"{'*'*70}")


if __name__ == "__main__":
    main()
