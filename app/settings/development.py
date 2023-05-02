# Flask settings
DEBUG = True
DEVELOPMENT = True
SECRET_KEY = 'do-i-really-need-this'
SQLALCHEMY_DATABASE_URI = 'sqlite:///navlab.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
LANGUAGES = {
    'ca' : 'Català',
    'en' : 'English'
}
