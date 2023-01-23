from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    description: str
    status: str

    def archive(self):
        self.status = "archived"
