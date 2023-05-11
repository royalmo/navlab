from os import environ
def is_production():
    return 'PRODUCTION' in environ and environ['PRODUCTION'] == 'True'

if is_production():
    from .production import *
else:
    from .development import *
