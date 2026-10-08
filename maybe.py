tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("✅ Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("📭 No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("📭 No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_number = int(input("Enter task number to delete: "))

            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(f"🗑️ '{deleted_task}' deleted successfully!")
            else:
                print("❌ Invalid task number.")

    # Exit
    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.")
