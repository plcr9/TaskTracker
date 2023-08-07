from lib.task_list import TaskList

'''Initially, the incomplete tasks list is empty'''
def test_initially_incomplete_is_empty():
    tracker = TaskList()
    assert tracker.list_incomplete() == []

'''Initially, the complete tasks list is empty'''
def test_initially_complete_is_empty():
    tracker = TaskList()
    assert tracker.list_complete() == []