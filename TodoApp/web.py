import streamlit as st
import functions

def add_todo():
# Add new todo to the list
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

# Get the list of todos from the functions module
todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

# Initialize 'completed' state in session_state for todos if not already initialized
if 'completed' not in st.session_state:
    st.session_state['completed'] = {todo: False for todo in todos}

# Display todos with checkboxes
# Use a copy of the todos list to avoid modifying the list while iterating over it
for i, todo in enumerate(todos):
    checkbox_key = f"checkbox_{i}"
    checkbox = st.checkbox(todo, key=checkbox_key, value=st.session_state['completed'].get(todo, False))

    # Update the session_state with the current checkbox state
    st.session_state['completed'][todo] = checkbox
    
    if checkbox:
        todos.pop(i) 
        functions.write_todos(todos)  # Write the updated todos list
        st.rerun()  # Trigger rerun to reflect changes in the UI

# Input field to add new todos
st.text_input(label="", placeholder="Enter a todo", on_change=add_todo, key="new_todo")

st.session_state  # This is just for inspection in the UI, you can remove it if unnecessary
