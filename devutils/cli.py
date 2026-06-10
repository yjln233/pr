"""Command-line interface for DevUtils."""

import argparse
import sys

from devutils import __version__
from devutils.txtimer import run_timer
from devutils.fstats import show_stats
from devutils.passgen import generate_password


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="devutils",
        description="Handy developer utilities",
    )
    parser.add_argument(
        "--version", action="version", version=f"devutils {__version__}"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # txtimer
    timer_parser = subparsers.add_parser("txtimer", help="Time a command")
    timer_parser.add_argument(
        "cmd", nargs=argparse.REMAINDER, help="Command to time"
    )

    # fstats
    stats_parser = subparsers.add_parser("fstats", help="File/directory statistics")
    stats_parser.add_argument("path", nargs="?", default=".", help="Path to analyze")

    # passgen
    pass_parser = subparsers.add_parser("passgen", help="Generate a password")
    pass_parser.add_argument(
        "--length", "-l", type=int, default=20, help="Password length (default: 20)"
    )
    pass_parser.add_argument(
        "--count", "-c", type=int, default=1, help="Number of passwords (default: 1)"
    )

    args = parser.parse_args()

    if args.command == "txtimer":
        run_timer(args.cmd)
    elif args.command == "fstats":
        show_stats(args.path)
    elif args.command == "passgen":
        generate_password(args.length, args.count)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
