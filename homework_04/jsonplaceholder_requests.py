"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_json_data(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            json_data = await response.json()
            return json_data
