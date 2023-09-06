from src.db.models import Admin
from src.db.repositories.repository import SQLAlchemyRepository


class AdminRepository(SQLAlchemyRepository):
    model = Admin
