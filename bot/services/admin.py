from typing import List

from bot.schemas import AdminSchema
from bot.utils.repository import AbstractRepository


class AdminService:
    def __init__(self, admin_repo: AbstractRepository):
        self.admin_repo: AbstractRepository = admin_repo()

    async def get_admins(self) -> List[AdminSchema]:
        admins = await self.admin_repo.find_all()
        return admins

    async def get_admin(self, **filter_by) -> AdminSchema:
        admin = await self.admin_repo.find_one(**filter_by)
        return admin
