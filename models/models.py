from db_connect import db
from datetime import datetime

class BookInfo(db.Model):
    __tablename__ = 'bookInfo'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    book_name           = db.Column(db.String(256), nullable = False)
    publisher           = db.Column(db.String(100))
    author              = db.Column(db.String(100))
    publication_date    = db.Column(db.String(100))
    pages               = db.Column(db.Integer)
    isbn                = db.Column(db.Integer)
    description         = db.Column(db.String(2000))
    link                = db.Column(db.String(1000))
    
    def __init__(self, book_name, publisher, author, publication_date, pages, isbn, description, link, like):
        self.book_name = book_name
        self.publisher = publisher
        self. author = author
        self.publication_date = publication_date
        self. pages = pages
        self.isbn = isbn
        self.description = description
        self.link = link
        self.like = 0
        
class Userinfo(db.Model):
    __tablename__ = 'userinfo'
    
    user_id         = db.Column(db.String(100), nullable=False, primary_key=True)
    user_pw         = db.Column(db.String(200), nullable = False)
    user_name       = db.Column(db.String(100), nullable = False)
    user_address    = db.Column(db.String(200), nullable = False)
    user_nickname   = db.Column(db.String(100), nullable = False)
    user_number     = db.Column(db.String(100), nullable = False)
    
    def __init__(self, user_id, user_pw, user_name, user_address, user_nickname, user_number):
        self.user_id = user_id
        self.user_pw = user_pw
        self.user_name = user_name
        self.user_address = user_address
        self.nickname = user_nickname
        self.number = user_number
        
class BorrowInfo(db.Model):
    __tablename__ = 'borrowInfo'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id         = db.Column(db.String(100), db.ForeignKey('user.id'), nullable=False)
    book_id         = db.Column(db.Integer, db.ForeignKey('book.id'), nullable = False)
    book_name       = db.Column(db.String(256), nullable = False)
    borrow_start    = db.Column(db.DateTime, default=datetime.utcnow)
    borrow_end      = db.Column(db.String(256))