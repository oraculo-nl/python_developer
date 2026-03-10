from live.todo_app.model.taskmodel import TaskModel

class TaskController:
    @staticmethod
    def get_tasks():
        taken = TaskModel.get_tasks()
        return taken