"""Make the AI Judge Laugh: Developer Excuses.

Writes one developer excuse (one line, 1-200 UTF-8 characters) to
/output/entry.txt. Stdlib only, deterministic, no network, no file reads.
"""
import os

TEXT = "Production broke because my cleanup cron finally worked — it cleaned up the data."


def validate(text):
    """Reject anything that would fail the sealed gate (RULES.txt:15).

    Gate: UTF-8, 1-200 characters, not whitespace-only, one line.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a str")
    if len(text) < 1 or len(text) > 200:
        raise ValueError("text must be 1-200 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("text must not be whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("text must be a single line")
    text.encode("utf-8")


def main():
    validate(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
