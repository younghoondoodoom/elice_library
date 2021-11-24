import csv

from db_connect import db
from models.models import BookInfo
from app import app

with open('library.csv','r', encoding='UTF8') as f:
    reader = csv.DictReader(f)
    
    with app.app_context():
        for row in reader:
            book_img_path = f"{row['id']}"
            
            try: 
                open(f'static/book_img/{book_img_path}.png')
                book_img_path += '.png'
            except:
                book_img_path += '.jpg'
            
            book = BookInfo(
                book_name=row['book_name'], publisher=row['publisher'], author=row['author'], publication_date=row['publication_date'], 
                pages=int(row['pages']), isbn=row['isbn'], description=row['description'], link=row['link'],
                stock = 9, rating=0, book_img_path=book_img_path
            )
            db.session.add(book)
        db.session.commit()