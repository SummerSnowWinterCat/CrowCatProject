from flask import jsonify
import json
from flask import render_template, session, redirect, url_for, request, make_response
from . import crow_cat_main_blueprint  # 导入蓝图
from crow_cat.crow_cat_body import crow_cat_imagination as imagination


@crow_cat_main_blueprint.route('/')
def index_page():
    return render_template('crowcat.html')


@crow_cat_main_blueprint.route('/crow_cat')
def console_page():
    return render_template('crowcat_console.html', days=imagination.datetime_today_memory_day(2018, 10, 13))


@crow_cat_main_blueprint.route('/ajax_days', methods=['POST'])
def get_days():
    return jsonify(json.dumps(imagination.datetime_today_memory_day(2018, 10, 13)))
