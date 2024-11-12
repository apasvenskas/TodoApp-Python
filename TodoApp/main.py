
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n" # \n is a break in line for todos.txt

            file = open('todos.txt', 'r') # read the todos.txt file
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('todos.txt', 'w') # writes in todos.txt file
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open('todos.txt', 'r')
            todos = file.readline()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}. {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo# Acces the todos index at number value. 
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("You entered a wrong command")

print("Bye!")