# -------------------------------------
# Модуль с конфигурационными константами
# -------------------------------------

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# создаем объект конфига
class Configuration(object):
    # включение режима дебага
    DEBUG = True
    
    # доступ к БД
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # отключение треккинга
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # секретный верификационный ключ
    SECRET_KEY = 'very-secret-key'

    # пароль БД
    SECURITY_PASSWORD_SALT = 'salt'

    # метод шифрования
    SECURITY_PASSWORD_HASH = 'sha256_crypt'

    # подключаем тему bootswatch для bootstrap
    FLASK_ADMIN_SWATCH = 'simplex'

    # включаем автоматическую регистрацию запросов
    SQLALCHEMY_ECHO = True