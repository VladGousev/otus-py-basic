from flask import Blueprint

about_app = Blueprint(
    "about_app",
    __name__,
    url_prefix="/about",
)


@about_app.get("/")
def about_view():
    return "Homework #5 from OTUS PythonBasic"
