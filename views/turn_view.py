from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from models.models import *
from db_connect import db

bp = Blueprint('turn', __name__, url_prefix='/turn')

# 반납하기 페이지를 먼저 만들자구나
# 현재 session에 있는 user_id와 일치하는 대여기록을 전부 가져온다.
# for문을 돌며 거기에 맞는 book 정보를 모두 가져와 빈 리스트 안에 넣는다.
# 그 리스트를 html 페이지에 띄운다.
# 반납하기 버튼을 클릭할 경우 그 borrow기록에서 삭제하고 redirect를 한다.
@bp.route('/home')
def home():
    #페이지네이션을 띄우기 위해서는 그 책의 
    if session.get('user_id'):
        user_id = session['user_id']
        page = request.args.get('page', type=int, default=1)
        borrows = BorrowInfo.query.filter(BorrowInfo.user_id == user_id)
        pagination = borrows.paginate(page, per_page=8, error_out=False)
        borrow_list = pagination.items
        book_list = []
        
        for i in range(len(borrow_list)):
            book = BookInfo.query.filter(BookInfo.id == borrow_list[i].book_id).first()
            book_list.append((book, borrow_list[i]))
        
        return render_template('turn.html', book_list=book_list, pagination = pagination)
    else:
        flash('로그인 후 사용해주세요.')
        return redirect(url_for('user.login'))

@bp.route('/back/<int:book_id>')
def back(book_id):
    if session.get('user_id'):
        borrow_info = BorrowInfo.query.filter(BorrowInfo.book_id == book_id).first()
        book_info = BookInfo.query.filter(BookInfo.id == book_id).first()
        
        #반납 테이블에 넣어주기
        returninfo = ReturnInfo(user_id = session['user_id'], book_id = book_id, borrow_start = borrow_info.borrow_start, borrow_end = borrow_info.borrow_end, book_name = book_info.book_name)

        book_info.stock += 1
        db.session.delete(borrow_info)
        db.session.add(returninfo)
        db.session.commit()
        
        flash(f'"{book_info.book_name}"를 정상적으로 반납 되었습니다.')
        
        return redirect(url_for('turn.home'))
    else:
        flash('로그인 후 사용해주세요.')
        return redirect(url_for('user.login'))
