class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def remove_task(self, task_index):
        if task_index < 1 or task_index > len(self.tasks):
            print("Invalid task index.")
        else:
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed successfully!")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            task_manager.add_task(task)
        elif choice == '2':
            task_manager.list_tasks()
        elif choice == '3':
            task_manager.list_tasks()
            task_index = int(input("Enter the task index to remove: "))
            task_manager.remove_task(task_index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
