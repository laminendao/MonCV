import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'votre_cle_secrete'
    DATABASE = os.path.join(BASE_DIR, 'database.db')
