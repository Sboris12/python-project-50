import json
from pathlib import Path


def load_json(filename):
    """Загружает и парсит JSON-файл из папки data."""
    data_path = Path(__file__).parent / 'data' / filename

    if not data_path.exists():
        raise FileNotFoundError(f"JSON file not found: {data_path}")

    with open(data_path, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Ошибка парсинга JSON-файла {filename}: {e}")
