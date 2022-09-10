from pydantic import BaseModel

class Blog(BaseModel):
  title: str
  body: str

class BlogOut(BaseModel):
  title: str
  body: str
  id: str