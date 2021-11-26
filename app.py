import os 

from flask import Flask
from db_connect import db

app = Flask(__name__)

from views import main_view, user_view, detail_view, turn_view, history_view

app.register_blueprint(main_view.bp)
app.register_blueprint(user_view.bp)
app.register_blueprint(detail_view.bp)
app.register_blueprint(turn_view.bp)
app.register_blueprint(history_view.bp)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://younghoon:dudgns2684@localhost:3306/book_borrow?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = "OF6JFR5EZ8W4BQ14DRJQ263EER4YG5966E1GAMV4AGDGJ5AW5B"

app.secret_key = "OF6JFR5EZ8W4BQ14DRJQ263EER4YG5966E1GAMV4AGDGJ5AW5B"


db.init_app(app)



if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=False)