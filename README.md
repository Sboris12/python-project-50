### Hexlet tests and linter status:
[![Actions Status](https://github.com/Sboris12/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Sboris12/python-project-50/actions)

# Gendiff

**Gendiff** — консольная утилита и библиотека на Python для сравнения двух файлов в формате JSON.  
Выводит разницу между файлами в читаемом формате "diff".

---

## 📽 Демонстрация

[![asciinema](https://asciinema.org/a/91XRcZhadpawMiMZIg7LIiGPb.svg)](https://asciinema.org/a/91XRcZhadpawMiMZIg7LIiGPb)

---

## 📦 Установка

```bash
git clone https://github.com/your-username/python-project-50.git
cd python-project-50
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
```

---

## 🚀 Использование

### CLI

```bash
gendiff path/to/file1.json path/to/file2.json
```

Пример:

```bash
gendiff src/hexlet_code/data/file1.json src/hexlet_code/data/file2.json
```

Результат:

```
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

---

### Как библиотека

```python
from hexlet_code.gendiff import generate_diff

diff = generate_diff("file1.json", "file2.json")
print(diff)
```

---

## 🧪 Тестирование

```bash
pytest
```

---

## 🗂 Структура проекта

```
python-project-50/
├── src/
│   └── hexlet_code/
│       ├── __init__.py
│       ├── cli.py
│       ├── gendiff.py
│       └── main.py
├── tests/
│   └── test_solution.py
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## 🛠 TODO

- Поддержка YAML
- Форматированные/вложенные структуры
- Разные стили отображения (plain, stylish, JSON)

---

## 🧾 Лицензия

MIT License
