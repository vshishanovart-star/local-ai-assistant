from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = BASE_DIR / "output" / "prompts"


def main():
    if not PROMPTS_DIR.exists():
        print("No prompts found.")
        return

    files = sorted(
        PROMPTS_DIR.glob("*.txt"),
        key=lambda item: item.stat().st_mtime
    )

    if not files:
        print("No prompts found.")
        return

    last_file = files[-1]

    print("\nLast prompt:\n")
    print(last_file.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()