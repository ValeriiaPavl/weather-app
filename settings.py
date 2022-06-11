import os.path

basedir = os.path.abspath((os.path.dirname(__file__)))
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'weather.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = bytes(1234)