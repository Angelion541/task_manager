# tests/test_model_storage.py

import os

from models import Task
import storage

def test_create_and_serialize():
    task = Task("Навчитися Python", "Пройти курс", "2025-07-20", done=False)
    task_dict = task.to_dict()
    print("🔍 Словник з об'єкта:", task_dict)

    restored = Task.from_dict(task_dict)
    print("✅ Відновлено з dict:", restored.__dict__)

def test_save_and_load():
    tasks = [
        Task("Навчитися Python", "Пройти курс", "2025-07-20", done=False),
        Task("Зробити проект", "Реалізувати ідею", "2025-08-01", done=False)
    ]
    storage.save_tasks(tasks)
    
    loaded = storage.load_tasks()
    print("📂 Завантажено з JSON:")
    for task in loaded:
        print(" -", task.__dict__)

def cleanup():
    file_path = "data/tasks.json"
    if os.path.exists(file_path):
        os.remove(file_path)
        print("🗑️ Тестовий файл видалено.")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    test_create_and_serialize()
    test_save_and_load()
    cleanup()