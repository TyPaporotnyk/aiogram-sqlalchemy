from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router(name="author-router")


@router.message(
    CommandStart(),
)
async def admin_start(message: Message):
    await message.answer(
        "Hi there! This is a simple clicker bot. Tap on green ball, but don't tap on red ones!\n"
        "If you tap a red ball, you'll have to start over.\n\n"
        "Enough talk. Just tap /play and have fun!"
    )
