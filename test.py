class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self._load_tasks()

    def _load_tasks(self):
        """Loads tasks from a file (private helper method)."""
        try:
            with open(self.filename, 'r') as f:
                self.tasks = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            self.tasks = []

    def _save_tasks(self):
        """Saves tasks to a file (private helper method)."""
        with open(self.filename, 'w') as f:
            for task in self.tasks:
                f.write(task + '\n')

    def add_task(self, new_task):
        """Adds a new task to the list and saves."""
        self.tasks.append(new_task)
        self._save_tasks()
        print(f"Task '{new_task}' added.")

    def list_tasks(self):
        """Lists all current tasks with their indices."""
        if not self.tasks:
            print("No tasks found.")
            return
        print("\n--- Your Tasks ---")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")
        print("------------------")
