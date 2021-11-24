from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from models.models import *
from db_connect import db

bp = Blueprint('history', __name__, url_prefix='/history')

@bp.route('/home')
def history():
    if session.get('user_id'):
        page = request.args.get('page', type=int, default=1)
        borrows = ReturnInfo.query.filter(ReturnInfo.user_id == session['user_id']).order_by(ReturnInfo.borrow_start.desc())
        pagination = borrows.paginate(page, per_page=8, error_out=False)
        borrow_list = pagination.items
        book_list = []
        
        for i in range(len(borrow_list)):
            book = BookInfo.query.filter(BookInfo.id == borrow_list[i].book_id).first()
            book_list.append((book, borrow_list[i]))
            
        return render_template('history.html', book_list=book_list, pagination = pagination)
    
    else:
        flash('로그인 후 사용해주세요.')
        return redirect(url_for('user.login'))

@bp.route('/search', methods=["POST"])
def search():
    if session.get('user_id'):
        keyword = request.form['title']
        search = ReturnInfo.query.filter(ReturnInfo.book_name.like(f"%{keyword}%")).order_by(ReturnInfo.borrow_start.desc())
        page = request.args.get('page', type=int)
        pagination = search.paginate(page, per_page=8, error_out=False)
        borrow_list = pagination.items
        book_list = []
        
        for i in range(len(borrow_list)):
            book = BookInfo.query.filter(BookInfo.id == borrow_list[i].book_id).first()
            book_list.append((book, borrow_list[i]))
        
        return render_template('history.html', book_list=book_list, pagination = pagination)