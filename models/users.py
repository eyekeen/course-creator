from .db_session import SqlAlchemyBase
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
import datetime
from sqlalchemy.orm import relationship, Mapped
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin, SqlAlchemyBase):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String, nullable=True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    email = Column(String, nullable=True)
    photo_id = Column(Integer, ForeignKey("photos.id"), nullable=True)
    hashed_password = Column(String, nullable=True)
    created_at = Column(DateTime,
                           nullable=True, default=datetime.datetime.now)
    tests: Mapped[list["Test"]] = relationship(back_populates="user")
    groups: Mapped[list["Group"]] = relationship(back_populates="user")
    histories: Mapped[list["History"]] = relationship(back_populates="user")

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)