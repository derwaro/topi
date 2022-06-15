from flask import render_template, flash, redirect, url_for, request
from topibox import db
from topibox.main import bp
from topibox.models import *
from topibox.main.forms import *
#additional imports:
import datetime

@bp.route('/')
@bp.route('/index')
def index():
    context = {}
    context["datetime"] = datetime.datetime.now()
    return render_template("index.html", context=context)