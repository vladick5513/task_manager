from typing import List, Optional
from app.models import Task
from app.storage import Storage

class TaskManager:
    """
    Класс для управления задачами.
    Обеспечивает функции добавления, удаления, редактирования, поиска и просмотра задач.
    """
    def __init__(self, storage_file: str) -> None:
        """
        Инициализация TaskManager.
        """
        self.storage = Storage(storage_file)
        self.tasks: List[Task] = self.storage.load_tasks()

    def add_task(self, title: str, description: str, category: str, due_date: str, priority: str) -> None:
        """
        Добавление новой задачи.
        """
        Task.validate_task_data(title, description, category, due_date, priority)
        task_id: int = len(self.tasks) + 1
        task = Task(task_id, title, description, category, due_date, priority)
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        print("Задача добавлена!")

    def view_tasks(self, category: Optional[str] = None) -> None:
        """
        Просмотр всех задач или задач по категории.
        """
        filtered_tasks: List[Task] = self.tasks if not category else [t for t in self.tasks if t.category == category]
        if not filtered_tasks:
            print(f"Список задач {'в категории ' + category if category else ''} пуст.")
        else:
            for task in filtered_tasks:
                print(task.to_dict())

    def mark_task_completed(self, task_id: int) -> None:
        """
        Пометка задачи как выполненной.
        """
        task = next((t for t in self.tasks if t.id == task_id), None)
        if not task:
            raise ValueError(f"Задача с ID {task_id} не найдена.")
        task.status = "Выполнена"
        self.storage.save_tasks(self.tasks)
        print("Статус задачи обновлен!")

    def edit_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                  category: Optional[str] = None, due_date: Optional[str] = None,
                  priority: Optional[str] = None) -> None:
        """
        Редактирование задачи.
        """
        task = next((t for t in self.tasks if t.id == task_id), None)
        if not task:
            raise ValueError(f"Задача с ID {task_id} не найдена.")
        if title:
            task.title = title
        if description:
            task.description = description
        if category:
            task.category = category
        if due_date:
            task.due_date = due_date
        if priority:
            task.priority = priority
        self.storage.save_tasks(self.tasks)
        print("Задача успешно отредактирована!")

    def delete_task(self, task_id: Optional[int] = None, category: Optional[str] = None) -> None:
        """
        Удаление задачи по ID или категории.
        """
        initial_count = len(self.tasks)
        if task_id:
            self.tasks = [t for t in self.tasks if t.id != task_id]
        elif category:
            self.tasks = [t for t in self.tasks if t.category != category]
        else:
            raise ValueError("Не указан ни ID задачи, ни категория для удаления.")
        if len(self.tasks) == initial_count:
            raise ValueError(
                f"Не найдена задача с ID {task_id}" if task_id else f"Нет задач в категории '{category}'.")
        self.storage.save_tasks(self.tasks)
        print("Удаление завершено.")

    def search_tasks(self, keyword: Optional[str] = None, category: Optional[str] = None,
                     status: Optional[str] = None) -> List[Task]:
        """
        Поиск задач по ключевым словам, категории и статусу.
        """
        results: List[Task] = self.tasks
        if keyword:
            results = [t for t in results if keyword.lower() in t.title.lower() or keyword.lower() in t.description.lower()]
        if category:
            results = [t for t in results if t.category == category]
        if status:
            results = [t for t in results if t.status.lower() == status.lower()]
        if not results:
            print("Задачи не найдены.")
        else:
            for task in results:
                print(task.to_dict())
        return results
