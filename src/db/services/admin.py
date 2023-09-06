from typing import List

from src.db.repositories.repository import AbstractRepository
from src.db.schemas import AdminSchema


class AdminService:
    def __init__(self, admin_repo: AbstractRepository):
        self.admin_repo: AbstractRepository = admin_repo()

    async def get_admins(self) -> List[AdminSchema]:
        admins = await self.admin_repo.find_all()
        return admins

    async def get_admin(self, **filter_by) -> AdminSchema:
        admin = await self.admin_repo.find_one(**filter_by)
        return admin
