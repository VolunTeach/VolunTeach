import os
from app import app

class Config:
    """Set Flask configuration"""

    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'