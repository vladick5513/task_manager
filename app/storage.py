import json
from typing import List
from app.models import Task

class Storage:
    """
    Класс для работы с хранилищем задач.
    """
    def __init__(self, file_path: str) -> None:
        """
        Инициализация хранилища.
        """
        self.file_path: str = file_path

    def load_tasks(self) -> List[Task]:
        """
        Загрузка задач из файла.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Task.from_dict(task_data) for task_data in data]
        except FileNotFoundError:
            print(f"Файл {self.file_path} не найден. Будет создан новый файл.")
            return []
        except json.JSONDecodeError as e:
            print(f"Ошибка чтения файла JSON: {e}")
            return []
        except Exception as e:
            print(f"Произошла ошибка при загрузке задач: {e}")
            return []

    def save_tasks(self, tasks: List[Task]) -> None:
        """
        Сохранение задач в файл.
        """
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump([task.to_dict() for task in tasks], file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Произошла ошибка при сохранении задач: {e}")

