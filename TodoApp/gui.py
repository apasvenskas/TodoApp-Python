import functions
import FreeSimpleGUI
import time

FreeSimpleGUI.theme("DarkBrown1")

clock = FreeSimpleGUI.Text('', key='clock_key')
label = FreeSimpleGUI.Text("Type in a todo")
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button = FreeSimpleGUI.Button("Add")
list_box = FreeSimpleGUI.Listbox(values = functions.get_todos(), 
                                 key = 'todos', 
                                 enable_events = True, 
                                 size = [45, 10])
edit_button = FreeSimpleGUI.Button("Edit")
complete_button = FreeSimpleGUI.Button("Complete")
exit_button = FreeSimpleGUI.Button("Exit")

window = FreeSimpleGUI.Window('My Todo App', 
                              layout=[
                                  [clock],
                                  [label], 
                                  [input_box, add_button], 
                                  [list_box, edit_button, complete_button], 
                                  [exit_button]
                                  ], 
                              font=('Helvetica', 18))
while True:
    event, values = window.read(timeout=200) # Displays the window on the screen.
    window["clock_key"].update(value=time.strftime("%b, %d, %Y, %H:%M:%S")) # displays the correct time in the clock variable 
    # print(event)
    # print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values = todos) #displays just added todo

        case "Edit":
            try:
                todo_edit = values['todos'][0]
                new_todo = values['todo'] 

                current_todo = functions.get_todos()
                index = current_todo.index(todo_edit)
                current_todo[index] = new_todo # updates the list with the new todo in gui
                functions.write_todos(current_todo)
                window['todos'].update(values = current_todo) #displays just added todo
            except IndexError: # For when user clicks edit without selected todo, program will output popup instead of crashing. 
                FreeSimpleGUI.popup("Please select and item first.", font=("Helvetica", 14)) # find the index error

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos) #send the todo to the functions.py file, write_todos function
                window["todos"].update(values = todos)
                window["todo"].update(value = "") #todo is a key for input_box
            except IndexError:
                FreeSimpleGUI.popup("Select a todo to complete.", font=("Helvetica", 14))

        case "Exit":
            break
        
        case 'todos':
            window['todo'].update(value = values['todos'][0])

        case FreeSimpleGUI.WIN_CLOSED:
            break

window.close()
