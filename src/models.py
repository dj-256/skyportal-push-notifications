from pydantic import BaseModel


class TokenEntry(BaseModel):
    userId: str
    token: str


class Message(BaseModel):
    title: str
    body: str
