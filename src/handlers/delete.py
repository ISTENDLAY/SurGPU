import aiohttp
from src.config.getting_data import token

async def deleteMessage(chat_id: int, message_id: int, TOKEN: str = token):
    async with aiohttp.ClientSession() as session:
        url = f'https://api.telegram.org/bot{TOKEN}/deleteMessage'
        async with session.get(url=url, params={'chat_id': chat_id, 'message_id': message_id}) as response:
            return await response.json()