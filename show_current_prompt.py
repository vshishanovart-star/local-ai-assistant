from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

PROMPT_FILE = (
    BASE_DIR / "output" / "current_prompt.txt"
)


def main():
    if not PROMPT_FILE.exists():
        print("Current prompt not found.")
        return

    content = PROMPT_FILE.read_text(
        encoding="utf-8"
    )

    print("\nCurrent Prompt:\n")
    print(content)


if __name__ == "__main__":
    main()