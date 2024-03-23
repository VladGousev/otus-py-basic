"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from jsonplaceholder_requests import (
    get_json_data,
    USERS_DATA_URL,
    POSTS_DATA_URL,
)
from models import Base, async_engine, Session, User, Post


async def init_db() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_user(user_data: dict, session: AsyncSession) -> None:
    user = User(
        name=user_data["name"],
        username=user_data["username"],
        email=user_data["email"],
    )
    session.add(user)
    await session.commit()


async def add_post(post_data: dict, session: AsyncSession) -> None:
    post = Post(
        user_id=post_data["userId"],
        title=post_data["title"],
        body=post_data["body"],
    )
    session.add(post)
    await session.commit()


async def create_users_and_posts(users_data: list, posts_data: list) -> None:
    async with Session() as session:
        for user in users_data:
            await add_user(user, session)
            for post in posts_data:
                if post["userId"] == user["id"]:
                    await add_post(post, session)


async def async_main():
    await init_db()
    users, posts = await asyncio.gather(
        get_json_data(USERS_DATA_URL), get_json_data(POSTS_DATA_URL)
    )
    await create_users_and_posts(users, posts)
    await async_engine.dispose()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
