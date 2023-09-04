import asyncio

from aiogram import Bot, Dispatcher
from config import config

from bot.handlers.admin import router as admin_router


async def main():
    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")
    await bot.delete_webhook(drop_pending_updates=True)

    dp = Dispatcher()
    dp.include_router(admin_router)

    # await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
