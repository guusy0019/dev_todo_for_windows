class ToDoDisplay:
    def display_todos(self, todos):
        if not todos:
            print("ToDoリストは空です。")
        else:
            print("ToDoリスト:")
            for i, todo in enumerate(todos, start=1):
                print(f"{i}. {todo}")
