from live.todo_app.controller.taskcontroller import TaskController

class TaskView:
    @staticmethod
    def show_menu():
        print("Menu")
        print("1. Add task")
        print("2. Show tasks")

    @staticmethod
    def menu_choice():
        choice = int(input("Choose an option: "))
        if choice == 1:
            pass
        elif choice == 2:
            TaskView.show_tasks()

    @staticmethod
    def show_tasks():
        # get tasks from database
        taken = TaskController.get_tasks()
        print("Tasks")
        print(taken)

