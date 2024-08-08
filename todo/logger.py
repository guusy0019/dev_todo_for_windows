import logging

# ログ設定
logging.basicConfig(
    filename='todo_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def get_logger():
    return logging.getLogger('ToDoApp')
