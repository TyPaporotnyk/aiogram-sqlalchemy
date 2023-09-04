from bot.models import Admin
from bot.utils.repository import SQLAlchemyRepository


class AdminRepository(SQLAlchemyRepository):
    model = Admin
