def get_todos(): 
    with open('todos.txt', 'r') as file: # Use 'a' to append to the file
        todos = file.readlines()
    return todos


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if 'add' in user_action:
        # todo = input("Enter a todo: ") + "\n" # \n is a break in line for todos.txt
        # todo = user_action[4:]
        # with open('todos.txt', 'a') as file: # Use 'a' to append to the file
        #     file.write(todo)

        if user_action.startswith("add"):
            todo = user_action[4:]

            todos = get_todos() #open todo.txt file via function get_todos

            todos.append(todo + '\n')

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

    elif 'show' in user_action:
        with open('todos.txt', 'r') as file: 
            todos = file.readlines() 
            new_todos = [item.strip('\n') for item in todos] 
                
            for index, item in enumerate(new_todos): 
                row = f"{index + 1}. {item}" 
                print(row)

    elif 'edit' in user_action:
        try:
            todos = get_todos()
            # with open('todos.txt', 'r') as file: 
            #     todos = file.readlines() 
                    
            new_todos = [item.strip('\n') for item in todos] 
            for index, item in enumerate(new_todos): 
                    row = f"{index + 1}. {item}" 
                    print(row)

            number = int(input("Enter the index number of the todo to edit: ")) - 1 
            new_todo = input("Enter new todo: ") + "\n" 


            todos[number] = new_todo 

            with open('todos.txt', 'w') as file: 
                file.writelines(todos)

                new_todos = [item.strip('\n') for item in todos] 
                for index, item in enumerate(new_todos): 
                    row = f"{index + 1}. {item}" 
                    print(row)
        except ValueError:
            print("Your command is not valid!")
            continue # restart the code             

    elif 'complete' in user_action:
        # with open('todos.txt', 'r') as file: 
        #     todos = file.readlines() 
        todos = get_todos()

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
            continue

    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid.")

print("Bye!")