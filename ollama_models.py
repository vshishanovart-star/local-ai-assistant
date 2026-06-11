import subprocess

from config_loader import load_config, save_config


def main():
    config = load_config()

    current_model = config["model"]

    result = subprocess.run(
        ["ollama", "list"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("Cannot get Ollama models.")
        return

    lines = result.stdout.strip().splitlines()

    if len(lines) <= 1:
        print("No models found.")
        return

    models = []

    print("\nOllama models:\n")

    for index, line in enumerate(lines[1:], start=1):
        model_name = line.split()[0]
        models.append(model_name)

        marker = " (current)" if model_name == current_model else ""
        print(f"{index} - {model_name}{marker}")

    choice = input("\nChoose model number or press Enter to cancel: ").strip()

    if not choice:
        return

    if not choice.isdigit():
        print("Invalid choice.")
        return

    index = int(choice)

    if index < 1 or index > len(models):
        print("Model number out of range.")
        return

    config["model"] = models[index - 1]
    save_config(config)

    print(f"\nCurrent model changed to: {models[index - 1]}")


if __name__ == "__main__":
    main()