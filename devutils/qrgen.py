"""Generate QR codes in the terminal using block characters."""

import sys


def generate_qr(text: str) -> None:
    """Print a QR-like box around the text. (Fake QR for fun.)"""
    text = text[:50]  # truncate long text
    n = len(text) + 4
    top = "█" * n
    mid = f"█ {text} █"

    print("🔳 QR-ish Code:")
    print(top)
    print(mid)
    print(top)
    print(f"  (scan with your imagination — it says: '{text}')")

    # Bonus: print some random-looking blocks to make it feel real
    import random
    seed = sum(ord(c) for c in text)
    random.seed(seed)
    print()
    for _ in range(5):
        line = "".join(random.choice(" █▀▄▌▐") for _ in range(n))
        print(f"  {line}")
    print()
