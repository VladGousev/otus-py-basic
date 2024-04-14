from sqlalchemy import select

from models.db import db
from models.user import User


def create_user(name: str) -> User:
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return user


def get_users() -> list[User]:
    return list(db.session.scalars(select(User)).all())


def delete_user(user: User) -> None:
    db.session.delete(user)
    db.session.commit()
