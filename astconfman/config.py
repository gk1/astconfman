import os

ADMINS = {
    'admin': dict(password='test', email='litnimax@pbxware.ru'),
}

ASTERISK_IPADDR = '127.0.0.1'

DEBUG = False
SQLALCHEMY_ECHO = False
DATABASE_FILE = os.path.join(os.path.dirname(__file__), 'astconfman.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
SECRET_KEY = 'change_me_here_to_random_key'
LANGUAGE = 'ru'

LOG_ENABLED = True
LOG_FILE = os.path.join(os.path.dirname(__name__), 'astconfman.log')

SMTP_LOG_ENABLED = False
SMTP_HOST = 'smtp.google.com'
SMTP_PORT = 587
SMTP_FROM = 'yourid@gmail.com'

# Asterisk
ASTERISK_SPOOL_DIR = '/var/spool/asterisk/outgoing/'
ASTERISK_MONITOR_DIR = '/var/spool/asterisk/monitor/'
ASTERISK_EXECUTABLE = '/usr/sbin/asterisk'
# Callout template.
CALLOUT_TEMPLATE = """Channel: Local/%(number)s@confman-dialout
Context: confman-bridge
Extension: %(confnum)s
Priority: 1
MaxRetries: 0
RetryTime: 15
WaitTime: 30
Set: participant_name=%(name)s
Set: participant_number=%(number)s
Set: conf_number=%(confnum)s
"""