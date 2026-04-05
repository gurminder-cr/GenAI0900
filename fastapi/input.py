from pydantic import BaseModel  # pydantic is used to fetch data from the host


class getData(BaseModel):
    name:str