import pathlib

path_to_db = pathlib.Path('.', 'weather.db').resolve()
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(path_to_db)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = bytes(1234)
