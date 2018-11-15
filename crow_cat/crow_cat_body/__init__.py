# -*- coding: utf-8 -*
from flask import Blueprint

crow_cat_main_blueprint = Blueprint('crow_cat_main_blueprint',__name__)

from . import crow_cat_errors, crow_cat_views
