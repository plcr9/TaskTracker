from lib.task import Task 

'''When task constructed with a title, the title is refleted in the title property'''
def test_constructs_with_a_title():
    task = Task("Clear the shed")
    assert task.title == "Clear the shed"

'''When task constructed, the task is initially incomplete'''
def test_task_is_initially_incomplete():
    task = Task("Clear the shed")
    assert task.complete == False

'''When task is marked as complete, it is complete'''
def test_marks_complete():
    task = Task("Clear the shed")
    task.mark_complete()
    assert task.complete == True