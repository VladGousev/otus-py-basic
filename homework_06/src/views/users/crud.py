from sqlalchemy import select

from models.db import db
from models.user import User


def create_user(name: str, username: str, email: str) -> User:
    user = User(name=name, username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


def get_users() -> list[User]:
    return list(db.session.scalars(select(User)).all())


def update_user(user: User) -> User:
    db.session.add(user)
    user.verified = True
    db.session.commit()
    return user


def delete_user(user: User) -> None:
    db.session.delete(user)
    db.session.commit()
