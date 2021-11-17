from flask import Flask
from db_connect import db
from views import main_view, user_view, detail_view

app = Flask(__name__)

app.register_blueprint(main_view.bp)
app.register_blueprint(user_view.bp)
app.register_blueprint(detail_view.bp)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:dudgns2684@127.0.0.1:3306/book_borrow" #꼭 내 루트 비밀번호로 바꿔줘야 함!!
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

app.secret_key = "dudgns2684"

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)