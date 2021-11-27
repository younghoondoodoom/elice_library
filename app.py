from flask import Flask
from db_connect import db

app = Flask(__name__)

from views import main_view, user_view, detail_view, turn_view, history_view

app.register_blueprint(main_view.bp)
app.register_blueprint(user_view.bp)
app.register_blueprint(detail_view.bp)
app.register_blueprint(turn_view.bp)
app.register_blueprint(history_view.bp)

app.config.from_pyfile('config.py')



db.init_app(app)



if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=False)