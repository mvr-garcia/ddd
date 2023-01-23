from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

    def change_password(self, new_password: str):
        self.password = new_password
