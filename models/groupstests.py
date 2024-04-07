from .db_session import SqlAlchemyBase
from sqlalchemy import Column, ForeignKey, Table


GroupsTests = Table(
    "groups_tests",
    SqlAlchemyBase.metadata,
    Column("group_id", ForeignKey("groups.id")),
    Column("test_id", ForeignKey("tests.id"))
)

