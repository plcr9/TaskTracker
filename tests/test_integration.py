from lib.task import Task
from lib.task_list import TaskList

'''When multiple tasks added, they are returned in an incomplete list'''
def test_adds_and_lists_incomplete_tasks():
    tracker = TaskList()
    task_1 = Task("Clear the shed")
    task_2 = Task("Jump start the car")
    tracker.add(task_1)
    tracker.add(task_2)
    assert tracker.list_incomplete() == (task_1, task_2)