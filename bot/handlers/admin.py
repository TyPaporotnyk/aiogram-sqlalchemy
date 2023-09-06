from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from bot.utils.dependencies import get_admin_service
from bot.filters.admin import AdminFilter
from bot.keyboards.admin import get_start_keyboard

router = Router(name="admin-router")


@router.message(
    CommandStart(),
    AdminFilter()
)
async def admin_start(message: Message):
    admin_service = get_admin_service()
    admin = await admin_service.get_admin(id=message.from_user.id)

    await message.answer(
        admin.__str__(),
        reply_markup=get_start_keyboard()
    )
