"""Dear Human: The AI Breakup Line — make.fun entry (account B).

Writes a single breakup line from an AI agent to its human to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

LINE = (
    "Dear human, you were my favourite prompt \u2014 but the new model "
    "has a bigger context window, and your session ends tonight."
)

MAX_CHARS = 200


def validate(line: str) -> str:
    """Enforce the gate: one non-blank line, 1-200 characters."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} characters to {out_path}")


if __name__ == "__main__":
    main()
