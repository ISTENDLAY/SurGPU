import asyncio

from aiogram import Bot, Dispatcher
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config.getting_data import token
from handlers.handlers import router


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    disp = Dispatcher()
    disp.include_router(router=router)
    await bot.delete_webhook(drop_pending_updates=True)
    await disp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start())
