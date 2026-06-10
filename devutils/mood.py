"""Daily developer mood checker. Very scientific."""

import random
import datetime


def check_mood() -> None:
    """Print today's developer mood forecast."""
    moods = [
        ("☕", "Caffeinated — ready to refactor everything"),
        ("🐛", "Bug-hunting mode — no bug is safe"),
        ("🚀", "Shipping velocity: maximum"),
        ("🧘", "Zen — it compiles on the first try"),
        ("🤖", "Feeling like an AI copilot"),
        ("💤", "Needs more sleep (coffee levels critical)"),
        ("🎉", "It works! No idea why, but it works!"),
        ("📚", "Learning mode — docs are your friend today"),
        ("🔥", "On fire — 10x engineer mode activated"),
        ("🦆", "Rubber duck debugging energy"),
    ]
    today = datetime.date.today()
    seed = today.toordinal()
    random.seed(seed)
    emoji, desc = random.choice(moods)
    print(f"📅 {today}")
    print(f"  {emoji}  {desc}")
    print(f"  Seed: {seed} (deterministic per day)")
