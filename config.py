import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'app.db'))  # db 접속 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"