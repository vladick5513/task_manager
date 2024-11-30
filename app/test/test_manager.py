import pytest

def test_add_task(task_manager):
    task_manager.add_task(
        title="Тестовая задача",
        description="Это описание тестовой задачи",
        category="Работа",
        due_date="2024-12-01",
        priority="Высокий"
    )
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0].title == "Тестовая задача"

def test_mark_task_completed(task_manager):
    task_manager.add_task(
        title="Тестовая задача",
        description="Это описание тестовой задачи",
        category="Работа",
        due_date="2024-12-01",
        priority="Высокий"
    )
    task_manager.mark_task_completed(task_id=1)
    assert task_manager.tasks[0].status == "Выполнена"

def test_search_tasks_by_keyword(task_manager):
    task_manager.add_task("Изучить Python", "Изучить основы языка Python", "Обучение", "2024-12-10", "Высокий")
    task_manager.add_task("Рабочая задача", "Закончить отчет", "Работа", "2024-12-05", "Средний")
    results = task_manager.search_tasks(keyword="Python")
    assert len(results) == 1
    assert results[0].title == "Изучить Python"

def test_search_tasks_by_category(task_manager):
    task_manager.add_task("Задача А", "Описание задачи А", "Работа", "2024-12-10", "Низкий")
    task_manager.add_task("Задача Б", "Описание задачи Б", "Личное", "2024-12-05", "Высокий")
    results = task_manager.search_tasks(category="Работа")
    assert len(results) == 1
    assert results[0].category == "Работа"


def test_delete_task(task_manager):
    task_manager.add_task("Удаляемая задача", "Описание задачи для удаления", "Работа", "2024-12-01", "Низкий")
    task_manager.delete_task(task_id=1)
    assert len(task_manager.tasks) == 0


def test_delete_task_invalid_id(task_manager):
    task_manager.add_task("Существующая задача", "Описание задачи", "Работа", "2024-12-01", "Низкий")
    with pytest.raises(ValueError, match="Не найдена задача с ID 999"):
        task_manager.delete_task(task_id=999)

def test_invalid_date(task_manager):
    with pytest.raises(ValueError, match="Дата должна быть в формате ГГГГ-ММ-ДД"):
        task_manager.add_task("Задача", "Описание задачи", "Работа", "неправильная-дата", "Высокий")



def test_empty_fields(task_manager):
    with pytest.raises(ValueError, match="Название задачи не может быть пустым."):
        task_manager.add_task("", "Описание задачи", "Работа", "2024-12-01", "Высокий")