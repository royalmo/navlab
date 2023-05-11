# Flask settings
DEBUG = False
DEVELOPMENT = False
SECRET_KEY = 'please-change-this-in-prod'
SQLALCHEMY_DATABASE_URI = 'sqlite:///navlab.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
LANGUAGES = {
    'ca' : 'Català',
    'en' : 'English'
}
SMTP_PASSWORD = ''
