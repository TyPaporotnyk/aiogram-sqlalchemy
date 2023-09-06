from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    PrimaryKeyConstraint,
    String,
)
from sqlalchemy.orm import relationship

from src.db import Base
from src.db.schemas import AuthorSchema, SpecialitySchema


class AuthorSpeciality(Base):
    __tablename__ = "author_speciality"
    __table_args__ = (PrimaryKeyConstraint("author_id", "speciality_id"),)

    author_id = Column(BigInteger, ForeignKey("author.id"))
    speciality_id = Column(Integer, ForeignKey("speciality.id"))


class Author(Base):
    __tablename__ = "author"

    id = Column(BigInteger, primary_key=True, autoincrement=False, index=True)
    name = Column(String(255), nullable=False, index=True)
    surname = Column(String(255), nullable=False, index=True)
    card_number = Column(String(16), index=True)

    rating = Column(Integer, default=0)
    busyness = Column(Float, default=0)
    plane_busyness = Column(Float, default=10)

    admin_id = Column(BigInteger, ForeignKey("admin.id"))
    admin = relationship("Admin", back_populates="authors")

    is_active = Column(Boolean, default=True)

    def to_read_model(self) -> AuthorSchema:
        return AuthorSchema(
            id=self.id,
            name=self.name,
            surname=self.surname,
            card_number=self.card_number,
            rating=self.rating,
            busyness=self.busyness,
            plane_busyness=self.plane_busyness,
            admin_id=self.admin_id,
            is_active=self.is_active,
        )


class Speciality(Base):
    __tablename__ = "speciality"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)

    def to_read_model(self) -> SpecialitySchema:
        return SpecialitySchema(
            id=self.id,
            name=self.name,
        )
