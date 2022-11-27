from pydantic import BaseModel


class Item(BaseModel):
    id: int
    alert_cateogry: str
    subcategory: str

    class Config:
        orm_mode = True
