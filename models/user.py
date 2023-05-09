from datetime import datetime
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str

class User(BaseModel):
    id: str
    email: str
    first_name: str
    middle_name: str
    last_name: str
    age: int
    sex: str
    address: Address
    profile_picture: str
    programme: str
    year: int
    emergency_number: str
    created_at: datetime
    last_active_at: datetime
