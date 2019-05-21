# -------------------------------------
# Запуск приложения
# -------------------------------------

import view
from app import app
from app import db
from posts.blueprint import posts

# подключаем блюпринт на функционал постов
app.register_blueprint(posts, url_prefix='/blog')

# инициализация приложения и запуск
if __name__ == '__main__':
    app.run()
    
