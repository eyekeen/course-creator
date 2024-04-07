from .db_session import SqlAlchemyBase
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship, Mapped
from .questionsanswers import QuestionsAnswers

class Answer(SqlAlchemyBase):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    is_correct = Column(Boolean, default=0)
    questions: Mapped[list["Question"]] = relationship(back_populates="answers", secondary=QuestionsAnswers)
