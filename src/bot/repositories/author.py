from src.bot.utils.repository import SQLAlchemyRepository
from src.db.models import Author


class AuthorRepository(SQLAlchemyRepository):
    model = Author
