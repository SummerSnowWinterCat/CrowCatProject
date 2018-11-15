# -*- coding: utf-8 -*
from flask import Flask
from config import config
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def crow_cat_create(config_name):
    crow_cat_flask = Flask(__name__)
    crow_cat_flask.config.from_object(config[config_name])  # 配置文件
    config[config_name].init_crow_cat(crow_cat_flask)
    bootstrap.init_app(crow_cat_flask)

    from .crow_cat_body import crow_cat_main_blueprint as crow_cat_main_blueprint
    crow_cat_flask.register_blueprint(crow_cat_main_blueprint)
    return crow_cat_flask
