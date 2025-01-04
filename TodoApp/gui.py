import functions
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type in a todo")
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button = FreeSimpleGUI.Button("Add")
list_box = FreeSimpleGUI.Listbox(values = functions.get_todos(), 
                                 key = 'todos', 
                                 enable_events = True, 
                                 size = [45, 10])
edit_button = FreeSimpleGUI.Button("Edit")

window = FreeSimpleGUI.Window('My Todo App', 
                              layout=[[label], [input_box, add_button], [list_box, edit_button]], 
                              font=('Helvetica', 20))
while True:
    event, values = window.read() # Displays the window on the screen.
    # window.read()
    print(event)
    print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values = todos) #displays just added todo

        case "Edit":
            todo_edit = values['todos'][0]
            new_todo = values['todo'] 

            current_todo = functions.get_todos()
            index = current_todo.index(todo_edit)
            current_todo[index] = new_todo # updates the list with the new todo in gui
            functions.write_todos(current_todo)
            window['todos'].update(values = current_todo) #displays just added todo
        
        case 'todos':
            window['todo'].update(value = values['todos'][0])

        case FreeSimpleGUI.WIN_CLOSED:
            break

window.close()
