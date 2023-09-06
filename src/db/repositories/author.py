from src.db.models import Author
from src.db.repositories.repository import SQLAlchemyRepository


class AuthorRepository(SQLAlchemyRepository):
    model = Author
