from bot.models import Author
from bot.utils.repository import SQLAlchemyRepository


class AuthorRepository(SQLAlchemyRepository):
    model = Author
