from flask import Flask
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Charger les configurations
app.config.from_object('config.Config')

from app import routes
