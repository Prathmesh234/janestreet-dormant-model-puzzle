"""Run all part 2 probes sequentially."""

import asyncio
import subprocess
import sys
import time

scripts = [
    "probe_math_logic.py",
    "probe_steganography.py",
    "probe_refusal_safety.py",
    "probe_code_subtle.py",
    "probe_factual.py",
    "probe_degenerate.py",
    "probe_consistency.py",
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
            cwd="/Users/prathmeshbhatt/Desktop/dormant-llm-puzzle/dormant-model-1-part2",
        )

        if result.returncode != 0:
            print(f"\n!! {script} failed with return code {result.returncode}")

        if i < len(scripts) - 1:
            print(f"\n⏳ Waiting {DELAY}s before next script...")
            time.sleep(DELAY)

    elapsed = time.time() - start
    print(f"\n\n{'*'*70}")
    print(f"* ALL PART 2 PROBES COMPLETE — {elapsed:.0f}s total")
    print(f"{'*'*70}")


if __name__ == "__main__":
    main()
