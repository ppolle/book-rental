import sys

if 'test' in sys.argv:
    from booker.settings.test import *
else:
    from booker.settings.custom import * 
