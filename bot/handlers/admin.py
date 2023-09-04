from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from bot.utils.dependencies import get_admin_service

router = Router(name="admin-router")


@router.message(CommandStart())
async def cmd_start(message: Message):
    admin_service = get_admin_service()
    admins = await admin_service.get_admins()
    print(admins)
    await message.answer(
        "Hi there! This is a simple clicker bot. Tap on green ball, but don't tap on red ones!\n"
        "If you tap a red ball, you'll have to start over.\n\n"
        "Enough talk. Just tap /play and have fun!"
    )
