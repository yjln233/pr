"""Show file and directory statistics."""

import os
from collections import Counter
from pathlib import Path


def _format_size(size_bytes: int) -> str:
    """Format bytes into a human-readable string."""
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} PB"


def show_stats(target: str) -> None:
    path = Path(target).resolve()

    if not path.exists():
        print(f"Error: path not found: {target}", file=None)
        return

    print(f"📊 Stats for: {path}")
    print("=" * 40)

    if path.is_file():
        stat = path.stat()
        print(f"  Type:        File")
        print(f"  Size:        {_format_size(stat.st_size)}")
        print(f"  Modified:    {stat.st_mtime}")
        return

    # Directory mode
    file_count = 0
    dir_count = 0
    total_size = 0
    ext_counter: Counter[str] = Counter()

    for root, dirs, files in os.walk(path):
        dir_count += len(dirs)
        for f in files:
            file_count += 1
            fp = Path(root) / f
            try:
                size = fp.stat().st_size
                total_size += size
                ext_counter[fp.suffix.lower() or "(no ext)"] += 1
            except OSError:
                pass

    print(f"  Files:       {file_count}")
    print(f"  Directories: {dir_count}")
    print(f"  Total size:  {_format_size(total_size)}")

    if ext_counter:
        print(f"\n  File types (top 10):")
        for ext, count in ext_counter.most_common(10):
            bar = "█" * min(count, 30)
            print(f"    {ext:<15} {count:>5}  {bar}")
