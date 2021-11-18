from db_connect import db
from datetime import datetime

class BookInfo(db.Model):
    __tablename__ = 'bookinfo'
    
    id                  = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    book_name           = db.Column(db.String(256), nullable = False)
    publisher           = db.Column(db.String(100))
    author              = db.Column(db.String(100))
    publication_date    = db.Column(db.String(100))
    pages               = db.Column(db.Integer)
    isbn                = db.Column(db.Integer)
    description         = db.Column(db.String(2000))
    link                = db.Column(db.String(1000))
    stock               = db.Column(db.Integer, default=9)
    rating              = db.Column(db.Integer, default=0)
    book_img_path       = db.Column(db.String(50))
    
    def __init__(self, book_name, publisher, author, publication_date, pages, isbn, description, link, stock, rating, book_img_path):
        self.book_name = book_name
        self.publisher = publisher
        self.author = author
        self.publication_date = publication_date
        self.pages = pages
        self.isbn = isbn
        self.description = description
        self.link = link
        self.stock = stock
        self.rating = rating
        self.book_img_path = book_img_path
        
class UserInfo(db.Model):
    __tablename__ = 'userinfo'
    
    user_id         = db.Column(db.String(100), nullable=False, primary_key=True)
    user_pw         = db.Column(db.String(200), nullable = False)
    user_nickname   = db.Column(db.String(100), nullable = False)
    user_number     = db.Column(db.String(100), nullable = False)
    
    def __init__(self, user_id, user_pw, user_number, user_nickname):
        self.user_id = user_id
        self.user_pw = user_pw
        self.user_number = user_number
        self.user_nickname = user_nickname
        
class BorrowInfo(db.Model):
    __tablename__ = 'borrowinfo'
    
    id              = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id         = db.Column(db.String(100), db.ForeignKey('userinfo.user_id'), nullable=False)
    book_id         = db.Column(db.Integer, db.ForeignKey('bookinfo.id'), nullable = False)
    book_name       = db.Column(db.String(256), nullable = False)
    borrow_start    = db.Column(db.DateTime, default=datetime.utcnow)
    borrow_end      = db.Column(db.DateTime)

    
class BookReview(db.Model):
    __tablename__ = 'bookreview'
    
    id              = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    user_id         = db.Column(db.String(100), db.ForeignKey('userinfo.user_id'), nullable=False)
    book_id         = db.Column(db.Integer, db.ForeignKey('bookinfo.id'), nullable=False)
    rating          = db.Column(db.Float)
    content         = db.Column(db.String(2000))
    update_time     = db.Column(db.DateTime, default=datetime.utcnow)
    