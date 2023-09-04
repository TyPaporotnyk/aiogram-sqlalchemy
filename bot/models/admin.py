from sqlalchemy import Boolean, Column, Integer

from bot.db import Base
from bot.schemas import AdminSchema


class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=False, index=True)
    is_active = Column(Boolean, default=True)

    def to_read_model(self) -> AdminSchema:
        return AdminSchema(
            id=self.id,
            is_active=self.is_active,
        )
