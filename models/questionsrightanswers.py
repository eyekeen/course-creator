from .db_session import SqlAlchemyBase
from sqlalchemy import Column, ForeignKey, Table, Integer, Float, Boolean


class QuestionsRightAnswers(SqlAlchemyBase):
    __tablename__ = "questions_right_answers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    rightanswer_id = Column(Integer, ForeignKey("answers.id"))
    test_id = Column(Integer, ForeignKey("tests.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))

