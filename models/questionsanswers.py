from .db_session import SqlAlchemyBase
from sqlalchemy import Column, ForeignKey, Table


QuestionsAnswers = Table(
    "questions_answers",
    SqlAlchemyBase.metadata,
    Column("answer_id", ForeignKey("answers.id")),
    Column("question_id", ForeignKey("questions.id"))
)

