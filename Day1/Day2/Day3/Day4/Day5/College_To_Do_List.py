tasks = ["presemtation", "assignment", "exam preparation"]

while True:
    print(" College To-Do List ")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
    
    elif choice == "2":
        task = input("Enter task to remove: ")

        if task in tasks:
            tasks.remove(task)
        
        else:
            print("Task not found!")

    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
