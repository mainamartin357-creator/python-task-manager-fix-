class Task:
    def __init__(self, id, title, description=""):
        self.id = id
        self.title = title
        self.description = description

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description=""):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        return task.id

    def delete_task(self, task_id):
        # BUG: Off-by-one error after pop()
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                return True
        return False

    def list_tasks(self):
        return [f"ID: {t.id} - {t.title}" for t in self.tasks]

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

if __name__ == "__main__":
    tm = TaskManager()
    print("Task Manager Ready")
