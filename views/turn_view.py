from flask import Blueprint, render_template, request, url_for, session, redirect, flash, g
from models.models import *
from db_connect import db
import datetime

bp = Blueprint('turn', __name__, url_prefix='/turn')

# 반납하기 페이지를 먼저 만들자구나
# 현재 session에 있는 user_id와 일치하는 대여기록을 전부 가져온다.
# for문을 돌며 거기에 맞는 book 정보를 모두 가져와 빈 리스트 안에 넣는다.
# 그 리스트를 html 페이지에 띄운다.
# 반납하기 버튼을 클릭할 경우 그 borrow기록에서 삭제하고 redirect를 한다.
@bp.route('/')
def home():
    user_id = session['user_id']
    borrows = BorrowInfo.query.filter(BorrowInfo.user_id == user_id).all()
    book_list = []
    
    for borrow in borrows:
        book = BookInfo.query.filter(BookInfo.id == borrow.book_id).first()
        book_list.append(book)
    
    return render_template('turn.html', book_list=book_list, borrows = borrows)

@bp.route('/back/<int:book_id>')
def back(book_id):
    borrow_info = BorrowInfo.query.filter(BorrowInfo.book_id == book_id).first()
    book_info = BookInfo.query.filter(BookInfo.id == book_id).first()
    book_info.stock += 1
    db.session.delete(borrow_info)
    db.session.commit()
    
    flash('정상적으로 반납 되었습니다.')
    
    return redirect(url_for('turn.home'))