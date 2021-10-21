from fastapi import FastAPI 
from pydantic import BaseModel

import requests

app = FastAPI()
##app = FastAPI(docs_url = None) turns off docs for security purposes

naturaldisasterdb = []

class NaturalDisaster(BaseModel):
    disastertype: str
    magnitudeorcategory: float
    location: str

@app.get('/')
def index():
    return {'key' : 'value'}

@app.get('/disasters')
def get_disasters():
    results = []
    for disaster in naturaldisasterdb:
        results.append({'disastertype' : disaster['disastertype'], 'magnitudeorcategory': disaster['magnitudeorcategory'], 'location': disaster['location']})
    return results

@app.get('/disasters/{disaster_id}')
def get_disaster(disaster_id: int):
    disaster = naturaldisasterdb[disaster_id - 1]
    return ({'disastertype' : disaster['disastertype'], 'magnitudeorcategory': disaster['magnitudeorcategory'], 'location': disaster['location']})

@app.post('/disasters')
def create_disasters(disaster: NaturalDisaster):
    naturaldisasterdb.append(disaster.dict())
    return naturaldisasterdb[-1]

@app.delete('/disasters/{disaster_id}')
def delete_disaster(disaster_id: int):
    naturaldisasterdb.pop(disaster_id - 1)
    return {}

##Use commands "pipenv install hypercorn", "pipenv shell", "pipenv install fastapi", "pipenv install requests", and "hypercorn main:app --reload" to use the 
##program. Then, go to 127.0.0.1:8080/docs in an Internet browser.