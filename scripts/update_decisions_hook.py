#!/usr/bin/env python3
"""Append relevant decisions to DECISIONS.md from either a commit message or direct input."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import threading
from pathlib import Path

TIMEOUT_SECONDS = 60


def git_root() -> Path:
    try:
        root = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        return Path(root)
    except subprocess.CalledProcessError:
        raise


def parse_decision(message: str):
    if "Decision:" not in message and "decision:" not in message:
        return None

    pattern = re.compile(
        r"Decision\s*:\s*(.+?)(?:\r?\n|$)\s*Reason\s*:\s*(.+?)(?:\r?\n|$)\s*Impact\s*:\s*(.+?)(?:\r?\n|$)",
        re.IGNORECASE | re.DOTALL,
    )
    match = pattern.search(message)
    if not match:
        return None

    return {
        "Decision": match.group(1).strip(),
        "Reason": match.group(2).strip(),
        "Impact": match.group(3).strip(),
    }


def append_decision(decision_file: Path, decision: dict[str, str]) -> None:
    block = (
        "Decision: " + decision["Decision"] + "\n"
        "Reason: " + decision["Reason"] + "\n"
        "Impact: " + decision["Impact"] + "\n\n"
    )
    with decision_file.open("a", encoding="utf-8") as handle:
        handle.write(block)


def read_last_commit_message(repo_root_path: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "log", "-1", "--pretty=%B"],
            cwd=str(repo_root_path),
            text=True,
        )
    except subprocess.CalledProcessError:
        return ""


def update_decisions(decision_file: Path, message: str) -> None:
    parsed = parse_decision(message)
    if parsed is None:
        return
    append_decision(decision_file, parsed)


def build_message_from_args(args: argparse.Namespace) -> str:
    if args.decision or args.reason or args.impact:
        return (
            "Decision: " + (args.decision or "") + "\n"
            "Reason: " + (args.reason or "") + "\n"
            "Impact: " + (args.impact or "")
        )
    return args.message or ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Append relevant decisions to DECISIONS.md.")
    parser.add_argument("--decision", help="Decision text to store.")
    parser.add_argument("--reason", help="Reason for the decision.")
    parser.add_argument("--impact", help="Impact of the decision.")
    parser.add_argument("--message", help="Commit message or decision block to parse.")
    parser.add_argument("--timeout", type=int, default=TIMEOUT_SECONDS, help="Max execution time in seconds.")
    args = parser.parse_args()

    try:
        repo_root_path = git_root()
    except subprocess.CalledProcessError:
        repo_root_path = Path.cwd()

    decision_file = repo_root_path / "DECISIONS.md"
    message = build_message_from_args(args)

    if not message.strip():
        message = read_last_commit_message(repo_root_path)

    parsed = parse_decision(message)
    if parsed is None:
        return 0

    result = {"error": None}

    def worker() -> None:
        try:
            update_decisions(decision_file, message)
        except Exception as exc:  # pragma: no cover - defensive handling
            result["error"] = exc

    thread = threading.Thread(target=worker, daemon=True)
    thread.start()
    thread.join(args.timeout)

    if thread.is_alive():
        print(f"Execution timed out after {args.timeout} seconds. DECISIONS.md update interrupted.", file=sys.stderr)
        return 124

    if result["error"] is not None:
        print(f"DECISIONS.md update failed: {result['error']}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
