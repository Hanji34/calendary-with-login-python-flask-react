import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'calendary-with-login-python-flask-react'