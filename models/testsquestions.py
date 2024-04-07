from .db_session import SqlAlchemyBase
from sqlalchemy import Column, ForeignKey, Table


TestsQuestions = Table(
    "tests_questions",
    SqlAlchemyBase.metadata,
    Column("test_id", ForeignKey("tests.id")),
    Column("question_id", ForeignKey("questions.id"))
)

