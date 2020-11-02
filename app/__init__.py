from flask import Flask

app = Flask(__name__)
app.config.from_object('config.Config')

from app import routes
from .Tutor import Tutor
from .Client import Client