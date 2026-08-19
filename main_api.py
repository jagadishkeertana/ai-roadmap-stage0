from fastapi import FastAPI
from pydantic import BaseModel
from clean_data import clean_row

app = FastAPI()

class PersonIn(BaseModel):
    name: str
    age: str


class PersonOut(BaseModel):
    name: str
    age: int


@app.post("/clean", response_model=list[PersonOut])
def clean_people(people: list[PersonIn]):
    cleaned = []
    for person in people:
        row = person.model_dump()
        result = clean_row(row)
        if result is not None:
            cleaned.append(result)
    return cleaned

@app.get("/")
def root():
    return {"status": "ok"}