import csv

from db_connect import db
from models.models import BookInfo

with open('library.csv','r') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        book_img_path = f"{row['id']}"
        
        try: 
            open(f'{book_img_path}.png')
            book_img_path += '.png'
        except:
            book_img_path += '.jpg'
        
        book = BookInfo(
            id=int(row['id']), name=row['book_name'], publisher=row['publisher'], author=row['author'], publication_date=row['publication_date'], 
            page_count=int(row['page_count'], isbn=row['isbn'], description=row['description'], book_img_path=book_img_path),
            stock = 9, rating=0
        )
        db.session.add(book)
    db.session.commit()