from aiogram.filters import BaseFilter
from aiogram.types import Message

from src.db.dependencies import get_admin_service


class AdminFilter(BaseFilter):
    async def __call__(self, obj: Message) -> bool:
        admin_service = get_admin_service()
        admin = await admin_service.get_admin(id=obj.from_user.id)

        return admin is not None
