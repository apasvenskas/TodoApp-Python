import functions
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type in a todo")
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button = FreeSimpleGUI.Button("Add")

window = FreeSimpleGUI.Window('My Todo App', 
                              layout=[[label], [input_box, add_button]], 
                              font=('Helvetica', 20))
while True:
    event, values = window.read() # Displays the window on the screen.
    # window.read()
    print(event)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case FreeSimpleGUI.WIN_CLOSED:
            break

window.close()
