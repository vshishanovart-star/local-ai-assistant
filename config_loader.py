import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = BASE_DIR / 'config.json'


def load_config():
    if not CONFIG_FILE.exists():
        print('Config file not found.')
        exit()

    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as file:
            config = json.load(file)

    except json.JSONDecodeError:
        print('Config file contains invalid JSON.')
        exit()

    required_keys = ['url', 'model', 'system_prompt', 'log_file']

    for key in required_keys:
        if key not in config:
            print(f'Missing config key: {key}')
            exit()

    if 'available_models' not in config:
        config['available_models'] = [config['model']]

    return config


def save_config(config):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as file:
        json.dump(config, file, ensure_ascii=False, indent=2)
