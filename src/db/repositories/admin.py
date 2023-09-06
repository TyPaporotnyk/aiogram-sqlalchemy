from src.db.repositories.repository import SQLAlchemyRepository
from src.db.models import Admin


class AdminRepository(SQLAlchemyRepository):
    model = Admin
