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

            number = int(input("Number of the todo to complete: ")) - 1 
            todos.pop(number) 
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'exit':
            break

        case _:
            print("You entered a wrong command")

print("Bye!")