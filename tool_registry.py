TOOLS = {
    "chat": {
        "type": "script",
        "target": "ai_memory_chat.py",
        "description": "Общение с локальной AI моделью."
    },

    "file_analyzer": {
        "type": "script",
        "target": "read_file_ai.py",
        "description": "Анализ файлов проекта, поиск ошибок и объяснение кода."
    },

    "project_overview": {
        "type": "script",
        "target": "project_overview_ai.py",
        "description": "Обзор структуры и архитектуры проекта."
    },

    "image_generation": {
        "type": "comfyui",
        "target": "open_comfyui",
        "description": "Создание изображений, логотипов, баннеров и иллюстраций."
    },

    "tts": {
        "type": "tts",
        "target": "open_qwen_tts",
        "description": "Озвучивание текста и создание аудио."
    }
}