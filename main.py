from typing import List
from fastapi import Depends, FastAPI, HTTPException
import firebase_admin

from src.db_ops import addNewEntry, getEntry
from src import models, schemas
from src.database import SessionLocal, engine

from src import fcm

schemas.Base.metadata.create_all(bind=engine)

default_app = firebase_admin.initialize_app()

app = FastAPI()

db = SessionLocal()


# Post a new token to the instance backend. This happens
# when a new user logs into the app.
@app.post("/token", response_model=models.TokenEntry)
def new_token(token_entry: models.TokenEntry):
    addNewEntry(db, token_entry)
    return token_entry


# Send a message to a user with a specific userId. This makes a call
# to the Firebase Cloud Messaging service to send a message to the user.
@app.post("/send/{userId}", response_model=models.TokenEntry)
def send_message(
    userId: str,
    message: models.Message,
):
    token_entry = getEntry(db, userId)
    if token_entry is None:
        raise HTTPException(status_code=404, detail="Token not found")
    fcm.send_message(token_entry.token, message.dict(), default_app)
    return token_entry


# Get all the tokens stored in the database. Just there for debugging purposes.
@app.get("/token", response_model=List[models.TokenEntry])
def read_token(skip: int = 0, limit: int = 100):
    return db.query(schemas.TokenEntry).offset(skip).limit(limit).all()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
