from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class TokenEntry(Base):
    __tablename__ = "token_entry"

    userId = Column(String, primary_key=True, index=True)
    token = Column(String, index=True)

    class Config:
        orm_mode = True
