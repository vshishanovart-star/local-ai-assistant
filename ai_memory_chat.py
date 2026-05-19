from datetime import datetime
from pathlib import Path

from config_loader import load_config
from logger import write_log
from ollama_client import ask_ollama


config = load_config()

url = config["url"]
model = config["model"]
system_prompt = config["system_prompt"]
log_file = config["log_file"]


messages = [
    {
        "role": "system",
        "content": system_prompt
    }
]

session_history = []

def show_recent_logs(lines_count=10):
    log_path = Path(log_file)

    if not log_path.exists():
        print("Log file not found.")
        return

    lines = log_path.read_text(encoding="utf-8").splitlines()
    recent_lines = lines[-lines_count:]

    if not recent_lines:
        print("Log file is empty.")
        return

    print("\nRecent logs:\n")

    for line in recent_lines:
        print(line)


def save_session():
    if not session_history:
        print("Session is empty. Nothing to save.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    session_file = f"logs/session_{timestamp}.txt"

    with open(session_file, "w", encoding="utf-8") as file:
        for item in session_history:
            file.write(item + "\n")

    print(f"Session saved to {session_file}")


while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    command = user_input.lower()

    if command in ["/exit", "exit"]:
        print("Chat stopped.")
        break

    if command in ["/help", "help"]:
        print("""
Commands:
/help   - show commands
/status - show assistant status
/history - show current session history
/logs    - show recent logs
/clear  - clear chat history
/save   - save current session
/exit   - exit chat
""")
        continue

    if command in ["/status", "status"]:
        print(f"""
Status:
Model: {model}
URL: {url}
Log file: {log_file}
Messages in memory: {len(messages)}
Session items: {len(session_history)}
""")
        continue

    if command in ["/history", "history"]:
        if not session_history:
            print("Session history is empty.")
        else:
            print("\nSession history:\n")

            for item in session_history:
                print(item)

        continue

    if command in ["/logs", "logs"]:
        show_recent_logs()
        continue

    if command in ["/clear", "clear"]:
        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]
        session_history = []
        print("Chat history cleared.")
        continue

    if command in ["/save", "save"]:
        save_session()
        continue

    messages.append({
        "role": "user",
        "content": user_input
    })

    write_log(log_file, "USER", user_input)

    session_history.append(f"USER: {user_input}")

    ai_message = ask_ollama(url, model, messages, timeout=120)

    print("\nAI:", ai_message)

    write_log(log_file, "AI", ai_message)

    session_history.append(f"AI: {ai_message}")

    messages.append({
        "role": "assistant",
        "content": ai_message
    })