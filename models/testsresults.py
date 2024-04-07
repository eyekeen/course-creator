from .db_session import SqlAlchemyBase
from sqlalchemy import Column, ForeignKey, Table


TestsResults = Table(
    "tests_results",
    SqlAlchemyBase.metadata,
    Column("result_id", ForeignKey("results.id")),
    Column("test_id", ForeignKey("tests.id"))
)

