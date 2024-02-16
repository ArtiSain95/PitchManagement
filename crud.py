from models import Pitch
from typing import List
from database import get_database
from validations import validate_next_maintenance_date, validate_replacement_date


async def create_pitch(pitch: Pitch) -> Pitch:
    """
    Create a new pitch and store it in the database.

    Args:
        pitch (Pitch): The details of the pitch.

    Raises:
        HTTPException: If validation checks for maintenance date or replacement date fail.

    Returns:
        Pitch: The created pitch.
    """
    db = get_database()
    validate_next_maintenance_date(pitch)
    validate_replacement_date(pitch)
    result = await db.pitches.insert_one(pitch.dict())
    created_pitch = await db.pitches.find_one({"_id": result.inserted_id})
    return created_pitch


async def get_all_pitches() -> List[Pitch]:
    """
    Retrieve all pitches from the database.

    Returns:
        List[Pitch]: List of all pitches.
    """
    db = get_database()
    pitches = await db.pitches.find().to_list(length=None)
    return pitches
