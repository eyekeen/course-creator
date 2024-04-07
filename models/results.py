from .db_session import SqlAlchemyBase
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped, relationship
from .testsresults import TestsResults


class Result(SqlAlchemyBase):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    tests: Mapped[list["Test"]] = relationship(back_populates="results", secondary=TestsResults)

