import json
import os

TODO_FILE = 'todo_list.json'

class ToDoStorage:
    def load_todos(self):
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, 'r') as file:
                return json.load(file)
        return []

    def save_todos(self, todos):
        with open(TODO_FILE, 'w') as file:
            json.dump(todos, file, indent=4)
