import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for i, todo in enumerate(todos):
    st.checkbox(todo, key=f"checkbox_{i}")

st.text_input(label="", placeholder="Enter a todo",
              on_change=add_todo, key="new_todo")

st.session_state