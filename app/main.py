from app.manager import TaskManager
from typing import Optional

def main() -> None:
    """
    Основная функция программы.
    Обеспечивает взаимодействие пользователя с TaskManager через консольное меню.
    """
    manager = TaskManager("tasks.json")

    while True:
        # Вывод основного меню действий
        print("\nМеню:")
        print("1. Просмотреть задачи")
        print("2. Добавить задачу")
        print("3. Изменить статус задачи")
        print("4. Удалить задачу")
        print("5. Поиск задач")
        print("6. Редактировать задачу")
        print("7. Выйти")
        choice: str = input("Выберите действие: ")

        try:
            # Просмотр задач с фильтрацией по категории
            if choice == "1":
                category: Optional[str] = input("Введите категорию для фильтрации (или нажмите Enter для всех задач): ")
                manager.view_tasks(category if category else None)

            # Добавление новой задачи
            elif choice == "2":
                title: str = input("Введите название задачи: ")
                description: str = input("Введите описание задачи: ")
                category: str = input("Введите категорию задачи: ")
                due_date: str = input("Введите срок выполнения (ГГГГ-ММ-ДД): ")
                priority: str = input("Введите приоритет (Низкий, Средний, Высокий): ")
                manager.add_task(title, description, category, due_date, priority)

            # Изменение статуса задачи
            elif choice == "3":
                task_id: int = int(input("Введите ID задачи: "))
                manager.mark_task_completed(task_id)

            # Удаление задачи по ID или категории
            elif choice == "4":
                delete_choice: str = input("Удалить по ID (1) или категории (2): ")
                if delete_choice == "1":
                    task_id: int = int(input("Введите ID задачи: "))
                    manager.delete_task(task_id=task_id)
                elif delete_choice == "2":
                    category: str = input("Введите категорию: ")
                    manager.delete_task(category=category)
                else:
                    print("Неверный выбор.")

            # Поиск задач по ключевым словам, категории и статусу
            elif choice == "5":
                keyword: Optional[str] = input("Введите ключевое слово для поиска (или оставьте пустым): ")
                category: Optional[str] = input("Введите категорию для фильтрации (или оставьте пустым): ")
                status: Optional[str] = input("Введите статус выполнения (Выполнена/Не выполнена, или оставьте пустым): ")
                manager.search_tasks(keyword, category, status)

            # Редактирование существующей задачи
            elif choice == "6":
                task_id: int = int(input("Введите ID задачи: "))
                title: Optional[str] = input("Введите новое название (или оставьте пустым): ")
                description: Optional[str] = input("Введите новое описание (или оставьте пустым): ")
                category: Optional[str] = input("Введите новую категорию (или оставьте пустым): ")
                due_date: Optional[str] = input("Введите новый срок выполнения (или оставьте пустым): ")
                priority: Optional[str] = input("Введите новый приоритет (или оставьте пустым): ")
                manager.edit_task(task_id, title, description, category, due_date, priority)

            # Завершение работы программы
            elif choice == "7":
                print("Выход из программы.")
                break
            else:
                print("Некорректный выбор.")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()