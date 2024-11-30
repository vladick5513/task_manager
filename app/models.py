from typing import Dict, Any
from datetime import datetime

class Task:
    """
    Класс для представления задачи.
    """
    def __init__(self, task_id: int, title: str, description: str, category: str, due_date: str, priority: str) -> None:
        """
        Инициализация задачи.
        """
        self.id: int = task_id
        self.title: str = title
        self.description: str = description
        self.category: str = category
        self.due_date: str = due_date
        self.priority: str = priority
        self.status: str = "Не выполнена"

    @staticmethod
    def validate_task_data(title: str, description: str, category: str, due_date: str, priority: str) -> None:
        """
        Проверка данных задачи на валидность.
        """
        if not title.strip():
            raise ValueError("Название задачи не может быть пустым.")
        if not description.strip():
            raise ValueError("Описание задачи не может быть пустым.")
        if not category.strip():
            raise ValueError("Категория задачи не может быть пустой.")
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД.")
        if priority not in ["Низкий", "Средний", "Высокий"]:
            raise ValueError("Приоритет задачи должен быть одним из: Низкий, Средний, Высокий.")

    def to_dict(self) -> Dict[str, Any]:
        """
        Преобразование задачи в словарь.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        """
        Создание экземпляра задачи из словаря.
        """
        required_fields = {"id", "title", "description", "category", "due_date", "priority", "status"}
        if not required_fields.issubset(data):
            raise ValueError(f"Некорректные данные для задачи. Требуемые поля: {required_fields}")
        task = cls(
            task_id=data["id"],
            title=data["title"],
            description=data["description"],
            category=data["category"],
            due_date=data["due_date"],
            priority=data["priority"],
        )
        task.status = data["status"]
        return task
