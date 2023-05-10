from flask_babel import Babel, Locale

babel = Babel(default_locale=Locale('en'))

def get_locales():
    locales = [Locale('en')] + babel.list_translations()
    return [(loc.language, loc.display_name.capitalize()) for loc in locales]
