import os
import pytest
from app.manager import TaskManager

# Фикстура для создания временного файла хранилища
@pytest.fixture
def task_manager():
    storage_file = "test_tasks.json"
    if os.path.exists(storage_file):
        os.remove(storage_file)
    manager = TaskManager(storage_file)
    yield manager
    if os.path.exists(storage_file):
        os.remove(storage_file)