from datetime import datetime, timezone
from fastapi import HTTPException, status
from models import Pitch

def validate_next_maintenance_date(pitch: Pitch):
    """
    Validate the next maintenance date based on the current pitch condition.

    Args:
        pitch (Pitch): The details of the pitch.

    Raises:
        HTTPException: If validation fails, raises a 400 Bad Request with a detailed error message.
    """
    if pitch.current_condition != 10 and pitch.next_maintenance_date >= datetime.now(timezone.utc):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="According to current condition, the next maintenance date does not match")
    
def validate_replacement_date(pitch: Pitch):
    """
    Validate the replacement date based on the current pitch condition.

    Args:
        pitch (Pitch): The details of the pitch.

    Raises:
        HTTPException: If validation fails, raises a 400 Bad Request with a detailed error message.
    """
    if pitch.current_condition <= 2 and pitch.replacement_date >= datetime.now(timezone.utc):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="According to current condition, the replacement date does not match")
