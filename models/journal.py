from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class JournalEntry(BaseModel):
    date: datetime
    description: str
    mood_value: str = Field(..., alias="mood_value")
    mood_score: float = Field(..., alias="mood_score")


class JournalModel(BaseModel):
    _id: str = Field(..., alias="_id")
    journal_entries: List[JournalEntry]


class CreateJournalEntryRequest(BaseModel):
    date: datetime
    description: str
    mood_value: str = Field(..., alias="mood_value")
    mood_score: float = Field(..., alias="mood_score") 


class CreateJournalEntryResponse(BaseModel):
    journal_entry: JournalEntry
