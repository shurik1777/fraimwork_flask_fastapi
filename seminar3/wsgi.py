from task_01 import app
# from lection3_additional_opportunity_flask.app_09 import app
"""
При обнаружении данного файла можно через консоль запускать простыми командами
проект на выполнение:
flask run
flask run --debug  # с дебагером
"""
if __name__ == '__main__':
    app.run(debug=True)
