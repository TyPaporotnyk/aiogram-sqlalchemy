from pydantic import BaseModel


class AdminSchema(BaseModel):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
