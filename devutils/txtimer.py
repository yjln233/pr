"""Time how long a command takes to run."""

import subprocess
import sys
import time


def run_timer(cmd: list[str]) -> None:
    if not cmd:
        print("Error: no command provided.", file=sys.stderr)
        print("Usage: devutils txtimer -- <command> [args...]", file=sys.stderr)
        sys.exit(1)

    print(f"⏱️  Timing: {' '.join(cmd)}")
    print("-" * 40)

    start = time.perf_counter()
    try:
        result = subprocess.run(cmd)
        exit_code = result.returncode
    except FileNotFoundError:
        print(f"Error: command not found: {cmd[0]}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        elapsed = time.perf_counter() - start
        print(f"\n⏹️  Interrupted after {elapsed:.3f}s")
        sys.exit(130)

    elapsed = time.perf_counter() - start

    print("-" * 40)
    print(f"⏱️  Elapsed: {elapsed:.3f}s")
    print(f"📋 Exit code: {exit_code}")

    if elapsed >= 60:
        minutes = int(elapsed // 60)
        seconds = elapsed % 60
        print(f"   ({minutes}m {seconds:.1f}s)")

    sys.exit(exit_code)
