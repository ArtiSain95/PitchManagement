from fastapi import FastAPI
from typing import List
from models import Pitch
from crud import create_pitch, get_all_pitches
from database import connect_to_mongo, close_mongo_connection

app = FastAPI()

# MongoDB connection
app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)


@app.post("/pitches/", response_model=Pitch)
async def create_pitch_handler(pitch: Pitch):
    """
    Create a new pitch.
    """
    return await create_pitch(pitch)

@app.get("/pitches/", response_model=List[Pitch])
async def get_all_pitches_handler():
    """
    Retrieve all pitches.
    """
    return await get_all_pitches()
