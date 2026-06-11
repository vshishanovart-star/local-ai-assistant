import subprocess
import sys
import webbrowser
from pathlib import Path

from config_loader import load_config, save_config


BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / 'logs' / 'chat_log.txt'
README_FILE = BASE_DIR / 'README.md'
OUTPUT_DIR = BASE_DIR / 'output'


def show_recent_tasks():
    run_script("recent_tasks.py")
    input("\nPress Enter to return to menu...")


def run_script(script_name):
    script_path = BASE_DIR / script_name
    subprocess.run([sys.executable, script_path], cwd=BASE_DIR)


def show_project_status():
    subprocess.run(['git', 'status'], cwd=BASE_DIR)


def show_recent_logs():
    if not LOG_FILE.exists():
        print('Log file not found.')
        input('\nPress Enter to return to menu...')
        return

    lines = LOG_FILE.read_text(encoding='utf-8').splitlines()

    if not lines:
        print('Log file is empty.')
        input('\nPress Enter to return to menu...')
        return

    print('\nRecent logs:\n')

    for line in lines[-20:]:
        print(line)

    input('\nPress Enter to return to menu...')


def show_project_files():
    print('\nProject files:\n')

    for item in BASE_DIR.iterdir():
        if item.name in ['.git', '.venv', '__pycache__']:
            continue

        if item.is_dir():
            print(f'[DIR]  {item.name}')
        else:
            print(f'[FILE] {item.name}')

    input('\nPress Enter to return to menu...')


def show_output_files():
    if not OUTPUT_DIR.exists():
        print('Output directory not found.')
        return

    files = [item for item in OUTPUT_DIR.iterdir() if item.is_file()]

    if not files:
        print('Output directory is empty.')
        return

    print('\nOutput files:\n')

    for item in sorted(files, key=lambda path: path.name.lower()):
        print(f'[FILE] {item.name}')

    input('\nPress Enter to return to menu...')


def show_readme():
    readme_path = BASE_DIR / 'README.md'

    if not readme_path.exists():
        print('README.md not found.')
        input('\nPress Enter to return to menu...')
        return

    content = readme_path.read_text(encoding='utf-8')

    print('\nREADME.md:\n')
    print(content)

    input('\nPress Enter to return to menu...')

def open_openwebui():
    webbrowser.open("http://localhost:3000")


def open_comfyui():
    subprocess.Popen(
        r"C:\AI\ComfyUI\ComfyUI_windows_portable\run_nvidia_gpu.bat",
        cwd=r"C:\AI\ComfyUI\ComfyUI_windows_portable",
        shell=True
    )


def open_qwen_tts():
    subprocess.Popen(
        [r"C:\AI\QweenTTS\Qwen3-TTS_portable_rus-main\portable\run.bat"],
        shell=True
    )


def change_model():
    run_script('ollama_models.py')


def main():
    while True:
        config = load_config()
        current_model = config['model']

        print(f'''
Local AI Assistant Menu

Current model: {current_model}

1 - Open local chat
2 - Analyze project file
3 - Show project status
4 - Show recent logs
5 - Show project files
6 - Analyze project overview
7 - Show README
8 - Run health check
9 - Show output files
10 - Change model
11 - AI Ecosystem Status
12 - Open Open WebUI
13 - Open ComfyUI
14 - Open Qwen3-TTS
15 - Start AI Ecosystem
16 - AI Task Router
17 - Recent Tasks
18 - Show Current Task
19 - Exit
''')

        choice = input('Choose option: ').strip()

        if choice == '1':
            run_script('ai_memory_chat.py')
            continue

        elif choice == '2':
            run_script('read_file_ai.py')
            continue

        elif choice == '3':
            show_project_status()
            continue

        elif choice == '4':
            show_recent_logs()
            continue

        elif choice == '5':
            show_project_files()
            continue

        elif choice == '6':
            run_script('project_overview_ai.py')
            continue

        elif choice == '7':
            show_readme()
            continue

        elif choice == '8':
            run_script('health_check.py')
            input('\nPress Enter to return to menu...')
            continue

        elif choice == '9':
            show_output_files()
            continue

        elif choice == '10':
            change_model()
            continue

        elif choice == '11':
            run_script('ecosystem_status.py')
            input('\nPress Enter to return to menu...')
            continue

        elif choice == '12':
            open_openwebui()
            continue

        elif choice == '13':
            open_comfyui()
            continue

        elif choice == '14':
            open_qwen_tts()
            continue

        elif choice == '15':
            open_openwebui()
            open_comfyui()
            open_qwen_tts()
            continue

        elif choice == '17':
            run_script('recent_tasks.py')
            input('\nPress Enter to return to menu...')
            continue

        elif choice == '18':
            run_script('show_current_task.py')
            input('\nPress Enter to return to menu...')
            continue

        if choice in ['19', 'exit', 'quit', 'q']:
            print('Menu closed.')
            break

        else:
            print('Unknown option. Try again.')


if __name__ == '__main__':
    main()
