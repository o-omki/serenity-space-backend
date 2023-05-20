from pydantic import BaseModel
from datetime import datetime
from bson import ObjectId
from typing import Optional

class Appointment(BaseModel):
    _id: Optional[str]
    user_id: str
    user_name: str
    user_picture: str
    confirmed: bool
    status: str
    appointment_date: str
    description: str
    created_at: str
    updated_at: str
    counsellor_id: str
    counsellor_name: str
    counsellor_picture: str
