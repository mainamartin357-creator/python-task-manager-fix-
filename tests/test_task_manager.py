import pytest
from main import TaskManager

def test_add_and_list_tasks():
    tm = TaskManager()
    tm.add_task("Task 1")
    tm.add_task("Task 2")
    tasks = tm.list_tasks()
    assert len(tasks) == 2
    assert "ID: 1 - Task 1" in tasks
    assert "ID: 2 - Task 2" in tasks

def test_delete_middle_task():
    tm = TaskManager()
    tm.add_task("Task 1")
    tm.add_task("Task 2")
    tm.add_task("Task 3")
    assert tm.delete_task(2) is True
    assert len(tm.list_tasks()) == 2
    assert "ID: 1 - Task 1" in tm.list_tasks()
    assert "ID: 3 - Task 3" in tm.list_tasks()

def test_delete_last_task():
    tm = TaskManager()
    tm.add_task("Task 1")
    tm.add_task("Task 2")
    assert tm.delete_task(2) is True
    assert len(tm.list_tasks()) == 1
    assert "ID: 1 - Task 1" in tm.list_tasks()

def test_multiple_deletions():
    tm = TaskManager()
    for i in range(1, 5):
        tm.add_task(f"Task {i}")
    assert tm.delete_task(2) is True
    assert tm.delete_task(4) is True
    assert len(tm.list_tasks()) == 2
    assert "ID: 1" in tm.list_tasks()[0]
    assert "ID: 3" in tm.list_tasks()[1]

def test_delete_nonexistent():
    tm = TaskManager()
    tm.add_task("Task 1")
    assert tm.delete_task(99) is False

def test_delete_first_task():
    tm = TaskManager()
    tm.add_task("Task 1")
    tm.add_task("Task 2")
    assert tm.delete_task(1) is True
    assert len(tm.list_tasks()) == 1
    assert "ID: 2 - Task 2" in tm.list_tasks()

def test_empty_list():
    tm = TaskManager()
    assert len(tm.list_tasks()) == 0
    assert tm.delete_task(1) is False
