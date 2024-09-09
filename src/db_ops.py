from sqlalchemy.orm import Session

from . import schemas, models


def addNewEntry(db: Session, token_entry: models.TokenEntry):
    db_token_entry = schemas.TokenEntry(
        userId=token_entry.userId, token=token_entry.token
    )
    db.add(db_token_entry)
    db.commit()
    db.refresh(db_token_entry)
    return db_token_entry


def getEntry(db: Session, userId: str):
    return (
        db.query(schemas.TokenEntry).filter(schemas.TokenEntry.userId == userId).first()
    )
