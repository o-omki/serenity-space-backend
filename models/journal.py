from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class JournalEntry(BaseModel):
    date: datetime
    description: str
    mood_value: str = Field(..., alias="mood_value")


class JournalModel(BaseModel):
    _id: str = Field(..., alias="_id")
    journal_entries: List[JournalEntry]


class CreateJournalEntryRequest(BaseModel):
    date: datetime
    description: str
    mood_value: str = Field(..., alias="mood_value")


class CreateJournalEntryResponse(BaseModel):
    journal_entry: JournalEntry
