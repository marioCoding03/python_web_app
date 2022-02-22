activate_this = '/home/ubuntu/.local/share/virtualenvs/WebPage-mBAPVMAS/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/WebPage')

from app import app as application
application.secret_key = 'password1234'
