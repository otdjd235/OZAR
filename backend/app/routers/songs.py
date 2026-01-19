from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.core.models.song import Song
from app.core.models.theme import Theme
from app.core.models.user import User
from app.core.permissions import requireAnyRole
from app.schemas.song import SongCreate

router = APIRouter(prefix="/songs", tags=["songs"])

@router.post("/")
def create_song(
    payload: SongCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(requireAnyRole(["ADMIN", "DIRECTOR", "LEAD"])),
):
    song = Song(
        title=payload.title.strip(),
        link=payload.link,
        lyrics=payload.lyrics,
        tonality=payload.tonality,
    )

    # Attacher aux thèmes
    if payload.theme_ids:
        themes = db.query(Theme).filter(Theme.id.in_(payload.theme_ids)).all()
        if len(themes) != len(set(payload.theme_ids)):
            raise HTTPException(status_code=400, detail="One or more theme_ids are invalid")
        song.themes = themes

    db.add(song)
    db.commit()
    db.refresh(song)

    # réponse simple (on peut faire response_model plus clean après)
    return {
        "id": song.id,
        "title": song.title,
        "link": song.link,
        "lyrics": song.lyrics,
        "tonality": song.tonality,
        "themes": [{"id": t.id, "title": t.title} for t in song.themes],
    }

@router.get("/")
def list_songs(db: Session = Depends(get_db)):
    songs = db.query(Song).all()
    return [
        {
            "id": s.id,
            "title": s.title,
            "link": s.link,
            "tonality": s.tonality,
            "themes": [{"id": t.id, "title": t.title} for t in s.themes],
        }
        for s in songs
    ]
