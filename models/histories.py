from .db_session import SqlAlchemyBase
from sqlalchemy import Column, Integer, DateTime, ForeignKey
import datetime
from sqlalchemy.orm import relationship, Mapped


class History(SqlAlchemyBase):
    __tablename__ = "histories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user: Mapped["User"] = relationship(back_populates="histories")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    result_id = Column(Integer, ForeignKey("results.id"), nullable=True)
    result: Mapped["Result"] = relationship()
    passed_at = Column(DateTime,
                           nullable=True, default=datetime.datetime.now)
