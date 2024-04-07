from .db_session import SqlAlchemyBase
from sqlalchemy import Column, ForeignKey, Table, Integer, Float, Boolean


class TestsRightAnswers(SqlAlchemyBase):
    __tablename__ = "tests_right_answers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    test_id = Column(Integer, ForeignKey("tests.id"))
    rightanswersnum = Column(Integer)
    fine = Column(Integer)