from sqlalchemy import select

from models.db import db
from models.user import User


def get_users() -> list[User]:
    return list(db.session.scalars(select(User)).all())
