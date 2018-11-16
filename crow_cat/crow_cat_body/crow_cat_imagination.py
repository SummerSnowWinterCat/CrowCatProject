from flask import request
import os
import datetime
import json


def visits_counts():
    return 0


def enter_password_check(passwd):
    print(passwd)

    return 0


def ip_search():
    ip_address = request.remote_addr
    if ip_address is None:
        return -1
    else:
        return ip_address


def secret_key_create():
    create_key = os.urandom(24)
    return create_key


def datetime_today_memory_day(y, m, d):
    day_1 = datetime.datetime(y, m, d)
    day_2 = datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
    days = (day_2 - day_1).days
    string_days = str(days)
    list = []
    for i in string_days:
        list.append(i)
    return list
