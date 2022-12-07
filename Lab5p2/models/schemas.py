from pydantic import BaseModel


class ArtistBase(BaseModel):
    name: str


class ArtistCreate(ArtistBase):
    pass


class Artist(ArtistBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class SongAlbumBase(BaseModel):
    name: str
    genre = str
    year = str
    element_type = enumerate
    parent_id = int


class SongAlbumCreate(SongAlbumBase):
    pass


class SongAlbum(SongAlbumBase):
    id: int

    class Config:
        orm_mode = True
