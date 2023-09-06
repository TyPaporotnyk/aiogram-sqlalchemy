import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aioredis.client import Redis

from config import config
from bot.utils import logging
from bot.handlers.admin import router as admin_router
from bot.handlers.author import router as author_router


async def main():
    logging.setup()

    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")
    await bot.delete_webhook(drop_pending_updates=True)

    redis_client = Redis.from_url(config.redis_url)
    storage = RedisStorage(redis=redis_client)

    dp = Dispatcher(storage=storage)
    dp.include_router(admin_router)
    dp.include_router(author_router)

    # await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
