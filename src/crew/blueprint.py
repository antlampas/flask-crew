from flask import Blueprint

crew_blueprint = Blueprint('crew',__name__,url_prefix='/crew',template_folder='templates',static_folder='static')