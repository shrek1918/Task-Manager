import sys

def add_task(task):
    try:
        with open("task.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    # Determine the new task number
    if lines:
        last_line = lines[-1].strip()
        last_number = int(last_line.split('.')[0])
        new_number = last_number + 1
    else:
        new_number = 1

    # Create the new task line with "false" status
    new_task_line = f"{new_number}. false. {task}\n"

    # Open the file in append mode and add the new task
    with open("task.txt", "a") as file:
        file.write(new_task_line)

    print(f"Task added: { new_task_line.strip().split('. ', 2)[2]}")


def display_tasks():
    try:
        with open("task.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No tasks found.")
        else:
            print("Incomplete Tasks:")
            for line in lines:
                # Split the line into task number, status, and description
                parts = line.strip().split('. ', 2)
                task_number = parts[0]
                status = parts[1]
                task_description = parts[2]

                # Display tasks with status "false"
                if status == "false":
                    print(f"{task_number}. {task_description}")

    except FileNotFoundError:
        print("The task.txt file does not exist.")

def mark_task_completed(task_number):
    try:
        with open("task.txt", "r") as file:
            lines = file.readlines()

        task_found = False

        for i, line in enumerate(lines):
            # Split the line into task number, status, and description
            parts = line.strip().split('. ', 2)
            current_task_number = parts[0]
            status = parts[1]
            task_description = parts[2]

            # Check if the current task number matches and status is "false"
            if current_task_number == str(task_number) and status == "false":
                # Mark the task as completed
                lines[i] = f"{current_task_number}. true. {task_description}\n"
                task_found = True
                break

        if task_found:
            # Write the updated task list back to the file
            with open("task.txt", "w") as file:
                file.writelines(lines)
            print(f"Task {task_number} marked as completed.")
        else:
            print(f"Task {task_number} is either already completed or does not exist.")

    except FileNotFoundError:
        print("The task.txt file does not exist.")

def remove_task(task_number):
    try:
        with open("task.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No tasks to remove.")
            return

        # Ensure the task number is valid
        if task_number < 1 or task_number > len(lines):
            print(f"Invalid task number: {task_number}")
            return

        # Remove the task
        removed_task = lines.pop(task_number - 1).strip()

        # Rewrite the file with updated task list
        with open("task.txt", "w") as file:
            for index, line in enumerate(lines):
                file.write(f"{index + 1}. {line.split('. ', 1)[1]}")

        print(f"Removed task: {removed_task.strip().split('. ', 2)[2]}")

    except FileNotFoundError:
        print("The task.txt file does not exist.")

if __name__ == "__main__":
    args = sys.argv
    if args[1] == 'add':
        add_task(args[2])
    elif args[1] == 'list':
        display_tasks()
    elif args[1] == 'complete':
        mark_task_completed(int(args[2]))
    elif args[1] == 'delete':
        remove_task(int(args[2]))
    else:
        print('Invalid command.')