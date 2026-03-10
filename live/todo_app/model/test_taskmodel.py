from taskmodel import TaskModel

def test_taskmodel():
    taken = TaskModel.get_tasks()
    begin_aantal_taken = len(taken)
    TaskModel.add_task("test")
    taken = TaskModel.get_tasks()
    nieuw_aantal_taken = len(taken)
    assert nieuw_aantal_taken == begin_aantal_taken + 1
    TaskModel.delete_task("test")
    taken = TaskModel.get_tasks()
    oud_aantal_taken = len(taken)
    assert oud_aantal_taken == begin_aantal_taken
