# from app_01 import app
from task_04 import app
"""
При обнаружении данного файла можно через консоль запускать простыми командами
проект на выполнение:
flask run
flask run --debug  # с дебагером
"""
if __name__ == '__main__':
    app.run(debug=True)
