"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    Mapped,
    mapped_column,
    relationship,
)

PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://postgres:password@localhost/postgres"
)

async_engine = create_async_engine(PG_CONN_URI, echo=False)
Session = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @classmethod
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


class User(Base):
    name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=True, unique=True)
    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
        cascade="all, delete, delete-orphan",
    )


class Post(Base):
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False
    )
    title: Mapped[str] = mapped_column(nullable=False)
    body: Mapped[str] = mapped_column(nullable=False)
    user = relationship("User", back_populates="posts", uselist=False)
