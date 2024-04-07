from .db_session import SqlAlchemyBase
from sqlalchemy import Column, ForeignKey, Table, Integer, Float


class AnswersResultsDeltas(SqlAlchemyBase):
    __tablename__ = "answers_results_deltas"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    answer_id = Column(Integer, ForeignKey("answers.id"))
    test_id = Column(Integer, ForeignKey("tests.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    result_id = Column(Integer, ForeignKey("results.id"))
    delta = Column("delta", Float)