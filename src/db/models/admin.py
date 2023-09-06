from sqlalchemy import BigInteger, Boolean, Column
from sqlalchemy.orm import relationship

from src.db import Base
from src.db.schemas import AdminSchema


class Admin(Base):
    __tablename__ = "admin"

    id = Column(BigInteger, primary_key=True, autoincrement=False, index=True)
    is_active = Column(Boolean, default=True)
    authors = relationship("Author", back_populates="admin")

    def to_read_model(self) -> AdminSchema:
        return AdminSchema(
            id=self.id,
            is_active=self.is_active,
        )
