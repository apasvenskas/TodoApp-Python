while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:

        case 'add':
            todo = input("Enter a todo: ") + "\n" # \n is a break in line for todos.txt
            with open('todos.txt', 'a') as file: # Use 'a' to append to the file
                file.write(todo)

        case 'show' | 'display':
            with open('todos.txt', 'r') as file: 
                todos = file.readlines() 
                new_todos = [item.strip('\n') for item in todos] 
                
                for index, item in enumerate(new_todos): 
                    row = f"{index + 1}. {item}" 
                    print(row)

        case 'edit':
            with open('todos.txt', 'r') as file: 
                todos = file.readlines() 
                number = int(input("Number of the todo to edit: ")) - 1 
                new_todo = input("Enter new todo: ") + "\n" 
                
                todos[number] = new_todo 
                with open('todos.txt', 'w') as file: 
                    file.writelines(todos)

        case 'complete':
            with open('todos.txt', 'r') as file: 
                todos = file.readlines() 

            try:
                number = int(input("Type the index number of the todo that was completed: ")) - 1
                todo_to_complete = todos[number].strip()
                confirm = input(f"Are you sure you want to complete '{todo_to_complete}'? (yes/no): ").strip().lower()

                if confirm in ('yes', 'y'):
                    todos.pop(number) # takes of the list
                    with open('todos.txt', 'w') as file: # reads tje list
                        file.writelines(todos)
                    print(f"Todo '{todo_to_complete}' marked as completed!")
                else:
                    print("Operation canceled.")
            except(IndexError, ValueError):
                print("Invalid number!")

        case 'exit':
            break

        case _:
            print("You entered a wrong command")

print("Bye!")