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
def complete_task(self, task_index):
        """Marks a task as complete (removes it) and saves."""
        if 0 <= task_index < len(self.tasks):
            completed_task = self.tasks.pop(task_index)
            self._save_tasks()
            print(f"Task '{completed_task}' marked as complete.")
            return True
        else:
            print("Invalid task number.")
            return False

    def delete_task(self, task_index):
        """Deletes a task from the list and saves."""
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            self._save_tasks()
            print(f"Task '{deleted_task}' deleted.")
            return True
        else:
            print("Invalid task number.")
            return False

task_manager = TaskManager() # Initialize the TaskManager instance

print("Welcome to your simple Task Manager!")

while True:
    print("\n--- Task Manager Menu ---")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("-------------------------")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        new_task_desc = input("Enter the task description: ")
        task_manager.add_task(new_task_desc)
    elif choice == 2:
        task_manager.list_tasks()
    elif choice == 3:
        task_manager.list_tasks()
        try:
            task_number_to_complete = int(input("Enter the number of the task to complete: ")) - 1
            task_manager.complete_task(task_number_to_complete)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == 4:
        task_manager.list_tasks()
        try:
            task_number_to_delete = int(input("Enter the number of the task to delete: ")) - 1
            task_manager.delete_task(task_number_to_delete)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == 5:
        print("Exiting Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    
# This implicitly handles the continuous operation and exit condition