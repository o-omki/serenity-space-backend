from datetime import datetime
from typing import List
from pydantic import BaseModel


class Contact(BaseModel):
    phone: str
    email: str
    address: dict


class Availability(BaseModel):
    days: List[str]
    hours: dict


class Rating(BaseModel):
    user_id: str
    rating: int
    comment: str
    date: datetime


class Review(BaseModel):
    user_id: str
    comment: str
    date: datetime


class Counsellor(BaseModel):
    _id: str
    name: str
    specialization: str
    experience: int
    num_sessions: int
    about: str
    contact: Contact
    availability: Availability
    qualifications: List[str]
    ratings: List[Rating]
    reviews: List[Review]
    created_at: datetime
    updated_at: datetime
    profile_picture: str
