from .db_session import SqlAlchemyBase
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
import datetime
from sqlalchemy.orm import relationship, Mapped
from .testsquestions import TestsQuestions
from .groupstests import GroupsTests
from .testsresults import TestsResults

class Test(SqlAlchemyBase):
    __tablename__ = "tests"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    title = Column(String, nullable=True)
    type_id = Column(Integer, nullable=True)
    user: Mapped["User"] = relationship(back_populates="tests")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    questions: Mapped[list["Question"]] = relationship(back_populates="tests", secondary=TestsQuestions)
    groups: Mapped[list["Group"]] = relationship(back_populates="tests", secondary=GroupsTests)
    created_at = Column(DateTime,
                           nullable=True, default=datetime.datetime.now)
    results: Mapped[list["Result"]] = relationship(back_populates="tests", secondary=TestsResults)