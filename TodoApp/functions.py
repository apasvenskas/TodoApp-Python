def get_todos(filepath="todos.txt"): # file path a general path witch can be specified in the call later such as todos = get_todos("todos.txt")
    """
        Read a text file and return the list of to do items.
    """
    with open(filepath, 'r') as file: # Use 'a' to append to the file
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath="todos.txt"):
     with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# print(help(get_todos))