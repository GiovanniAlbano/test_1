"""Command-line greeting example."""

import argparse


def greet(name: str = "World") -> str:
    """Return a friendly greeting for the supplied name."""
    return f"Hello, {name}!"


def main() -> None:
    """Parse command-line arguments and print a greeting."""
    parser = argparse.ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument("name", nargs="?", default="World", help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
