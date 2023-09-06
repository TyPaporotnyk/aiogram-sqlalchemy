from pydantic import BaseModel


class AuthorSchema(BaseModel):
    id: int
    name: str
    surname: str
    card_number: str
    rating: int
    busyness: float
    plane_busyness: float
    admin_id: int
    is_active: bool

    class Config:
        from_attributes = True


class SpecialitySchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
