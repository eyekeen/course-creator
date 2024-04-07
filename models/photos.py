from .db_session import SqlAlchemyBase
from sqlalchemy import Column, String, Integer


class Photo(SqlAlchemyBase):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String, nullable=True)