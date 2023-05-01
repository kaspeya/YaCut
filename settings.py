import os


class Config(object):
    # Подключается БД SQLite
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
    # Задаётся конкретное значение для конфигурационного ключа
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Всесто MY SECRET KEY придумайте и впишите свой ключ
    SECRET_KEY = os.getenv('SECRET_KEY')


MAX_LENGTH = 6
MAX_LEN_CUSTOM_ID = 16

HOST = 'localhost'

NO_REQUEST_BODY = 'Отсутствует тело запроса'
NO_REQUIRED_FIELD = '\"url\" является обязательным полем!'
INVALID_URL_NAME = 'Указано недопустимое имя для короткой ссылки'
NOT_FOUND = 'Указанный id не найден'

FORM_LEN_MSG = 'Короткая ссылка должна быть не более 16 символов'
FORM_REQUIRED_FIELD = 'Обязательное поле'
