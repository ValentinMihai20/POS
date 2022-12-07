from sqlalchemy.orm import Session
from models import artist_orm


def get_artists(db: Session):
    return db.query(artist_orm.Artists).all()


def get_artist_by_id(db: Session, uuid: int):
    return db.query(artist_orm.Artists).filter(artist_orm.Artists.uuid == uuid).first()


