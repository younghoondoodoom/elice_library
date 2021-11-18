from flask import Blueprint, render_template, request, url_for, session, redirect, flash, g
from models.models import *
from db_connect import db

bp = Blueprint('detail', __name__, url_prefix='/detail')


@bp.route('/<int:id>')
def home(id):
    book = BookInfo.query.filter(BookInfo.id == id).first()
    review_info = BookReview.query.filter(BookReview.book_id == id).all()
    
    rating_sum, average = 0, 0
    if review_info:
        for review in review_info:
            rating_sum += review.rating
        average = round(rating_sum / len(review_info), 1)
    
    book.rating = average
    db.session.commit()    
    
    

    if g.user:
        return render_template('book_detail.html', book = book, review_info = review_info, average = average)
    else:
        flash('로그인 후 이용해주세요.')
        return redirect(url_for('user.login'))
    
@bp.route('/write_review/<int:id>', methods=['POST'])
def write_review(id):
    if g.user:
        user_id = session['user_id']
        book_id = id
        rating = request.form['star']
        content = request.form['review']
        review = BookReview(user_id = user_id, book_id = book_id, content = content, rating = rating)
        db.session.add(review)
        db.session.commit()        
        
        flash('소중한 리뷰 감사합니다!')
        
        return redirect(url_for('detail.home', id = id))
    
@bp.route('/delete_review/<int:review_id>')
def delete_review(review_id):
    if 'user_id' not in session:
        flash('권한이 없습니다.')
        return redirect(url_for('user.login'))
    
    user_info = UserInfo.query.filter(UserInfo.user_id == session['user_id']).first()
    review_info = BookReview.query.filter(BookReview.id == review_id).first()
    
    if not review_info:
        flash('이미 삭제된 리뷰입니다.')
        return redirect(url_for('main.home'))
    if not user_info or review_info.user_id != session['user_id']:
        flash('권한이 없습니다.')
    
    db.session.delete(review_info)
    db.session.commit()
    
    flash('정상적으로 리뷰가 삭제 되었습니다.')
    
    book_info = BookInfo.query.filter(BookInfo.id == review_info.book_id).first()
    return redirect(url_for('detail.home', id = book_info.id))