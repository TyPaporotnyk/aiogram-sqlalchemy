from src.bot.utils.repository import SQLAlchemyRepository
from src.db.models import Admin


class AdminRepository(SQLAlchemyRepository):
    model = Admin
