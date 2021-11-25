from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from models.models import *
from db_connect import db
import datetime


bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    page = request.args.get('page', type=int, default=1)
    books = BookInfo.query.order_by(BookInfo.book_name.asc())
    pagination = books.paginate(page, per_page=8, error_out=False)
    book_list = pagination.items

    return render_template('main.html', book_list=book_list, pagination=pagination)


@bp.route('/search', methods=['POST'])
def search():
    keyword = request.form['title']
    search = BookInfo.query.filter(BookInfo.book_name.like(f"%{keyword}%"))
    page = request.args.get('page', type=int)
    pagination = search.paginate(page, per_page=8, error_out=False)
    book_list = pagination.items
    return render_template('main.html', book_list=book_list, pagination = pagination)
    

@bp.route('/borrow/<int:book_id>')
def borrow(book_id):
    if session.get('user_id') is None:
        flash('로그인 후 이용해주세요.')
        return redirect(url_for('main.home'))
    
    book = BookInfo.query.filter(BookInfo.id == book_id).first()
    user_id = session['user_id']
    book_name = book.book_name
    borrow = BorrowInfo(user_id = user_id, book_id = book_id, book_name = book_name)
    
    already_borrowed = BorrowInfo.query.filter(BorrowInfo.book_id == book_id).first()
    
    if already_borrowed:
        flash(f'"{book.book_name}"은 이미 대여한 책입니다.')
        return redirect(url_for('main.home'))
    
    if book.stock > 0:
        book.stock = book.stock - 1
        db.session.add(borrow)
        db.session.commit()
        endtime = BorrowInfo.query.filter(BorrowInfo.book_id == book_id).order_by(BorrowInfo.id.desc()).first()
        endtime.borrow_end = endtime.borrow_start + datetime.timedelta(days=7)
        db.session.commit()
        flash(f'"{book.book_name}"을 정상적으로 대여가 완료 되었습니다.')
    else:
        flash(f'"{book.book_name}"의 재고가 없습니다.')
    
    return redirect(url_for('main.home'))
