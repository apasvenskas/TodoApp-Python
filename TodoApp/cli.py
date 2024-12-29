import functions 
import time

currentDateTime = time.strftime("%b, %d, %Y, %H:%M:%S") # get the current time in desired format

print(currentDateTime)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if 'add' in user_action:
        if user_action.startswith("add"):

            todo = user_action[4:].strip()  # .strip() removes any unwanted leading/trailing spaces

            if todo:
                todos = functions.get_todos()
                # file path a general path witch can be specified in the call later such as todos = get_todos("todos.txt")
                todos.append(todo + '\n')
                functions.write_todos(todos)
                print(f"Todo added: {todo}")
            
            # if no todo is directly provided
            else:
                todo = input("Enter the todo to be added: ").strip()

                if todo:
                    todos = functions.get_todos()# file path a general path witch can be specified in the call later such as todos = get_todos("todos.txt")
                    todos.append(todo + '\n')
                    functions.write_todos(todos)
                    print(f"Todo added: {todo}")
                else:
                    print("Todo cannot be added.")

    elif 'show' in user_action:
        with open('todos.txt', 'r') as file: 
            todos = file.readlines() 
            new_todos = [item.strip('\n') for item in todos] 
                
            for index, item in enumerate(new_todos): 
                row = f"{index + 1}. {item}" 
                print(row)

    elif 'edit' in user_action:
        try:
            todos = functions.get_todos()# file path a general path witch can be specified in the call later such as todos = get_todos("todos.txt")
                    
            new_todos = [item.strip('\n') for item in todos] 
            for index, item in enumerate(new_todos): 
                    row = f"{index + 1}. {item}" 
                    print(row)

            number = int(input("Enter the index number of the todo to edit: ")) - 1 
            new_todo = input("Enter new todo: ") + "\n" 


            todos[number] = new_todo 

            functions.write_todos(todos)

            new_todos = [item.strip('\n') for item in todos] 
            for index, item in enumerate(new_todos): 
                row = f"{index + 1}. {item}" 
                print(row)

        except ValueError:
            print("Your command is not valid!")
            continue # restart the code             

    elif 'complete' in user_action:
        todos = functions.get_todos() # file path a general path witch can be specified in the call later such as todos = get_todos("todos.txt")

        try:
            number = int(input("Type the index number of the todo that was completed: ")) - 1
            todo_to_complete = todos[number].strip()
            confirm = input(f"Are you sure you want to complete '{todo_to_complete}'? (yes/no): ").strip().lower()

            if confirm in ('yes', 'y'):
                todos.pop(number) # takes of the list
                functions.write_todos(todos)
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