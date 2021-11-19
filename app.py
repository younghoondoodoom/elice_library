from flask import Flask
from db_connect import db
from views import main_view, user_view, detail_view, turn_view, history_view

app = Flask(__name__)

app.register_blueprint(main_view.bp)
app.register_blueprint(user_view.bp)
app.register_blueprint(detail_view.bp)
app.register_blueprint(turn_view.bp)
app.register_blueprint(history_view.bp)


db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)