from flask import Flask
from db_connect import db
import config
from views import main_view, user_view

app = Flask(__name__)

app.register_blueprint(main_view.bp)
app.register_blueprint(user_view.bp)




db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)