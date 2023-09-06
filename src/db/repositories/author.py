from src.db.repositories.repository import SQLAlchemyRepository
from src.db.models import Author


class AuthorRepository(SQLAlchemyRepository):
    model = Author
