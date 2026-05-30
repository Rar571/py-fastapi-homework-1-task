from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from online_cinema.models import  Movie
from online_cinema.schemas import MovieList, MovieCreate
from database import get_db


router = APIRouter()


@router.get("/movies/{movie_id}", response_model=MovieList)
async def get_film(film_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie).where(Movie.id == film_id))
    film = result.scalar_one_or_none()
    if not film:
        raise HTTPException(status_code=404, detail="Movie not found")


@router.post("/movies/", response_model=MovieList)
async def create_film(movie: MovieCreate, db: AsyncSession = Depends(get_db)):
    new_movie = Movie(**movie.model_dump())
    db.add(new_movie)
    await db.commit()
    await db.refresh(new_movie)
    return new_movie
