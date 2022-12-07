import models.artist_orm
from models.artist_orm import Artists
from models.song_album_orm import AlbumSongs
from base.sql_base_spotify import connect_to_db
from fastapi import HTTPException, FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import models.schemas as schemas
import models.crud as crud

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})


@app.get("/artists", status_code=200, response_model=schemas.Artist)  # vezi ca trebuie un dictionar de artisti aici
def get_artists(db: Session = Depends(connect_to_db)):
    try:
        return crud.get_artists(db)
    except ValueError:
        return HTTPException(status_code=404, detail='Artist not found')


@app.get("/artists/{uuid}", status_code=200, response_model=schemas.Artist)
def get_artist(uuid: int, db: Session = Depends(connect_to_db)):
    try:
        return crud.get_artist_by_id(db, uuid)
    except ValueError:
        return HTTPException(status_code=404, detail='Artist not found')


# @app.post("/artists", status_code=201, response_model=schemas.Artist)
# def post_artist(name, isactive,  db: Session = Depends(connect_to_db())):
#     try:
#         new_artist = Artist(name, isactive)
#         db.add(new_artist)
#         db.commit()
#     except ValueError:
#         return HTTPException(status_code=406, detail='Artist not properly defined')
#
#
