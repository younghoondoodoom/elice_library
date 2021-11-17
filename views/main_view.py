from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from models.models import *

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    book_list = BookInfo.query.order_by(BookInfo.book_name.asc()).all()
    return render_template('main.html', book_list=book_list)

