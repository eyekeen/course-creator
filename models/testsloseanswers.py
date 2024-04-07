from .db_session import SqlAlchemyBase
from sqlalchemy import Column, ForeignKey, Table, Integer, Float, Boolean


class TestLoseAnswers(SqlAlchemyBase):
    __tablename__ = "tests_loseanswers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    test_id = Column(Integer, ForeignKey("tests.id"))
    loseanswersnum = Column(Integer)
    fine = Column(Integer)
