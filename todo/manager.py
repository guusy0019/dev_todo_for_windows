from .storage import ToDoStorage
from .display import ToDoDisplay
from .logger import get_logger

class ToDoManager:
    def __init__(self):
        self.storage = ToDoStorage()
        self.display = ToDoDisplay()
        self.logger = get_logger()

    def add_todo(self):
        todo = input("新しいToDoを入力してください: ")
        todos = self.storage.load_todos()
        todos.append(todo)
        self.storage.save_todos(todos)
        self.logger.info(f"'{todo}' を追加しました。")
        print(f"'{todo}' を追加しました。")

    def remove_todo(self):
        todos = self.storage.load_todos()
        self.display.display_todos(todos)
        try:
            index = int(input("削除するToDoの番号を入力してください: ")) - 1
            if 0 <= index < len(todos):
                removed_todo = todos.pop(index)
                self.storage.save_todos(todos)
                self.logger.info(f"'{removed_todo}' を削除しました。")
                print(f"'{removed_todo}' を削除しました。")
            else:
                print("無効な番号です。")
        except ValueError:
            print("番号を正しく入力してください。")
