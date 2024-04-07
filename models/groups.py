from .db_session import SqlAlchemyBase
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from .groupstests import GroupsTests


class Group(SqlAlchemyBase):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    title = Column(String, nullable=True)
    tests: Mapped[list["Test"]] = relationship(back_populates="groups", secondary=GroupsTests)
    user: Mapped["User"] = relationship(back_populates="groups")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)