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

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = os.environ.get('SECRET_KEY')


db.init_app(app)



if __name__ == '__main__':
    app.run(debug=True)