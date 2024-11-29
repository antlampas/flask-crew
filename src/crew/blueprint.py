from flask      import Blueprint
from flask_menu import current_menu

crew_blueprint = Blueprint('crew',__name__,url_prefix='/crew',template_folder='templates',static_folder='static')
