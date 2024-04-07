from .db_session import SqlAlchemyBase
from sqlalchemy import Column, ForeignKey, Table


AnswersTests = Table(
    "answers_tests",
    SqlAlchemyBase.metadata,
    Column("answer_id", ForeignKey("answers.id")),
    Column("test_id", ForeignKey("tests.id"))
)

