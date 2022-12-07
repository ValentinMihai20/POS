from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship

from base.sql_base_spotify import Base
from models.join_table import artists_song_album_relationship
from models import song_album_orm


class Artists(Base):
    __tablename__ = 'artists'
    __table_args__ = {'extend_existing': True}

    uuid = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String(192))
    is_active = Column(Boolean)
    album_songs = relationship("models.song_album_orm.AlbumSongs", secondary=artists_song_album_relationship,
                               back_populates='artists')

    def __init__(self, name, isactive):
        self.name = name
        self.is_active = isactive

    def __repr__(self):
        return f'< Artist "{self.name}">'


