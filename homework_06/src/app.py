from flask import Flask, url_for, redirect
from flask_migrate import Migrate

import config
from models.db import db
from views.users.views import users_app

app = Flask(__name__)

app.config.update(
    SECRET_KEY="6fc01f2db60feff0f53537060",
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_ECHO=config.SQLALCHEMY_ECHO,
)

app.register_blueprint(
    users_app,
)

db.init_app(app)
migrate = Migrate(app, db)


@app.get("/", endpoint="index")
def index():
    url = url_for("users_app.list")
    return redirect(url)


if __name__ == "__main__":
    app.run(debug=True)
