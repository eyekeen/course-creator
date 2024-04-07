from .db_session import SqlAlchemyBase
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, Mapped
from .questionsanswers import QuestionsAnswers
from .testsquestions import TestsQuestions


class Question(SqlAlchemyBase):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    tests: Mapped[list["Test"]] = relationship(back_populates="questions", secondary=TestsQuestions)
    answers: Mapped[list["Answer"]] = relationship(back_populates="questions", secondary=QuestionsAnswers)