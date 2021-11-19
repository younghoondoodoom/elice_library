from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from models.models import *
from db_connect import db

bp = Blueprint('history', __name__, url_prefix='/history')

@bp.route('/home')
def history():
    if session.get('user_id'):
        borrow_list = ReturnInfo.query.filter(ReturnInfo.user_id == session['user_id']).order_by(ReturnInfo.borrow_start.desc()).all()
        book_list = []
        
        for i in range(len(borrow_list)):
            book = BookInfo.query.filter(BookInfo.id == borrow_list[i].book_id).first()
            book_list.append((book, borrow_list[i]))
            
        return render_template('history.html', book_list=book_list)
    
    else:
        flash('로그인 후 사용해주세요.')
        return redirect(url_for('user.login'))