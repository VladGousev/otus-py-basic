from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.exceptions import BadRequest

from models.user import User
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
        users=crud.get_users(),
    )


@users_app.route(
    "/add/",
    endpoint="add",
    methods=["GET", "POST"],
)
def create_user():
    if request.method == "GET":
        return render_template("users/add.html")

    user_name = request.form.get("user-name", "")
    user_name = user_name.strip()
    if not user_name:
        raise BadRequest("user-name is required!")

    user = crud.create_user(
        name=user_name,
    )

    url = url_for(
        "users_app.details",
        user_id=user.id,
    )
    return redirect(url)


@users_app.get(
    "/<int:user_id>/",
    endpoint="detail",
)
def get_user_detail(user_id: int):
    user: User = User.query.get_or_404(
        user_id,
        description=f"User #{user_id} not found!",
    )
    return render_template(
        "users/detail.html",
        user=user,
    )


@users_app.route(
    "/<int:user_id>/confirm-delete/",
    endpoint="delete",
    methods=["GET", "POST"],
)
def delete_user(user_id: int):
    user: User = User.query.get_or_404(
        user_id,
        description=f"User #{user_id} not found!",
    )
    if request.method == "GET":
        return render_template(
            "users/delete.html",
            user=user,
        )

    crud.delete_user(user)

    url = url_for("users_app.list")
    return redirect(url)
