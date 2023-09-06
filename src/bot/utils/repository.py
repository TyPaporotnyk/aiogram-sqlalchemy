from abc import ABC, abstractmethod

from sqlalchemy import insert, select
from sqlalchemy.exc import NoResultFound

from src.db.db import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, **filter_by):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            return res.scalar_one()

    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            try:
                res = await session.execute(stmt)
                res = [row[0].to_read_model() for row in res.all()]
                return res
            except NoResultFound:
                return []

    async def find_one(self, **filter_by):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**filter_by)
            try:
                res = await session.execute(stmt)
                res = res.scalar_one().to_read_model()
                return res
            except NoResultFound:
                return None
