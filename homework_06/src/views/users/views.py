from flask import Blueprint, render_template

from views.users import crud

users_app = Blueprint(
    "users_app",
    __name__,
    url_prefix="/users",
)


@users_app.get(
    "/",
    endpoint="list",
)
def get_users():
    return render_template(
        "users/list.html",
        products=crud.get_users(),
    )
