# storage.py

import json
from models import Task

FILE_PATH = 'data/tasks.json'

def load_tasks():
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [Task.from_dict(task) for task in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON data. Returning an empty task list.")
        return []

def save_tasks(tasks):
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump([task.to_dict() for task in tasks], file, ensure_ascii=False, indent=4)
