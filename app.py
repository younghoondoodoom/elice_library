from flask import Flask
from db_connect import db
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
from views import main_view, user_view, detail_view, turn_view, history_view

app.register_blueprint(main_view.bp)
app.register_blueprint(user_view.bp)
app.register_blueprint(detail_view.bp)
app.register_blueprint(turn_view.bp)
app.register_blueprint(history_view.bp)



csrf = CSRFProtect()
csrf.init_app(app)

db.init_app(app)



if __name__ == '__main__':
    app.run(debug=True)