def get_todos(Filepath="todos.txt"):
    with open(Filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,Filepath="todos.txt"):
    with open(Filepath, 'w') as file:
        file.writelines(todos_arg)