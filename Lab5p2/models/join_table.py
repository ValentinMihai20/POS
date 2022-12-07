from sqlalchemy import Column, Integer, Table, ForeignKey

from base.sql_base_spotify import Base

artists_song_album_relationship = Table(
    'artists_song_album_relationship', Base.metadata,
    Column('artist_id', Integer, ForeignKey('artists.uuid'), primary_key=True),
    Column('song_album_id', Integer, ForeignKey('album-songs.id'), primary_key=True),
    extend_existing=True
)
