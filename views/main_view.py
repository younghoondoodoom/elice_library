from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from models.models import *
import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    book_list = BookInfo.query.order_by(BookInfo.book_name.asc()).all()
    return render_template('main.html', book_list=book_list)

@bp.route('/borrow/<int:book_id>')
def borrow(book_id):
    book = BookInfo.query.filter(BookInfo.id == book_id).first()
    user_id = session['user_id']
    book_name = book.book_name
    borrow = BorrowInfo(user_id = user_id, book_id = book_id, book_name = book_name)
    if book.stock > 0:
        book.stock = book.stock - 1
        db.session.add(borrow)
        db.session.commit()
        endtime = BorrowInfo.query.filter(BorrowInfo.book_id == book_id).order_by(BorrowInfo.id.desc()).first()
        endtime.borrow_end = endtime.borrow_start + datetime.timedelta(days=7)
        db.session.commit()
        flash('정상적으로 대여가 완료 되었습니다.')
    else:
        flash(f'{book.book_name}의 재고가 없습니다.')
    
    return redirect(url_for('main.home'))