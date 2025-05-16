from pydantic import BaseModel
from typing import List

class ActorBase(BaseModel):
    actor_name: str

class ActorPublic(ActorBase):
    id: int

    class Config:
        orm_mode = True

class MovieBase(BaseModel):
    title: str
    year: int
    director: str
    actors: List[ActorBase]

class MoviePublic(MovieBase):
    id: int
    actors: List[ActorPublic]

    class Config:
        orm_mode = True

class SummaryRequest(BaseModel):
    movie_id: int

class SummaryResponse(BaseModel):
    summary_text: str
