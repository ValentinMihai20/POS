from sqlalchemy import Column, String, Integer, Enum, ForeignKey, Boolean, Table, create_engine
from sqlalchemy.orm import relationship, backref
from base.sql_base_spotify import Base
from models.join_table import artists_song_album_relationship
# from models.artist_orm import Artist


class AlbumSongs(Base):
    __tablename__ = 'album_songs'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(192))
    genre = Column(String(192))
    year = Column(String(5))
    element_type = Column(Enum('song', 'album', 'single'))
    parent_id = Column(Integer, ForeignKey('album_songs.id'))

    children = relationship("AlbumSongs", backref=backref("parent", remote_side=[id]))
    artists = relationship("models.artist_orm.Artists", secondary=artists_song_album_relationship,
                           back_populates='album_songs')

    def __init__(self, name, genre, year, element_type):
        self.name = name
        self.genre = genre
        self.year = year
        self.element_type = element_type

    def __repr__(self):
        return f'<"{self.element_type.capitalize()}" "{self.name}">'


# Base.metadata.create_all(create_engine('mariadb+pymysql://db-admin:db-admin@192.168.56.10:3306/spotify'))


