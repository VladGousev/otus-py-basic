from sqlalchemy.orm import Mapped, mapped_column

from models.db import db


class User(db.Model):
    name: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str | None] = mapped_column(unique=True)
    # posts = relationship(
    #     "Post",
    #     back_populates="user",
    #     uselist=True,
    #     cascade="all, delete, delete-orphan",
    # )
