from todo.manager import ToDoManager

def main():
    manager = ToDoManager()
    
    while True:
        print("\nToDoリスト メニュー:")
        print("1. ToDoを表示")
        print("2. ToDoを追加")
        print("3. ToDoを削除")
        print("4. 終了")
        choice = input("選択してください: ")

        if choice == '1':
            todos = manager.storage.load_todos()
            manager.display.display_todos(todos)
        elif choice == '2':
            manager.add_todo()
        elif choice == '3':
            manager.remove_todo()
        elif choice == '4':
            print("終了します。")
            break
        else:
            print("無効な選択です。もう一度試してください。")

if __name__ == "__main__":
    main()
