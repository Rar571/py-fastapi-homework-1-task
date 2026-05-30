from pydantic import BaseModel, ConfigDict


class MovieBase(BaseModel):
    title: str
    genre: str
    price: float


class MovieCreate(MovieBase):
    pass


class MovieList(MovieBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
