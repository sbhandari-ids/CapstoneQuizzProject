from flask import Blueprint

admin = Blueprint('admin', __name__ , template_folder='admin_templates')

from app.blueprints.admin import routes

from . import forms
