from flask import Blueprint, render_template, request, url_for, session, redirect
from db_connect import db
from models.models import *

bp = Blueprint('main', __name__)

@bp.route('/')
def main():
    return render_template('main.html')