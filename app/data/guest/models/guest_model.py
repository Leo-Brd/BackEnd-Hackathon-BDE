from sqlalchemy import Column, String, Integer

from shared import db


class GuestModel(db.Model):
    __tablename__ = "guest"
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False
    )
    username = Column(String(100))
    password = Column(String(255))
    
