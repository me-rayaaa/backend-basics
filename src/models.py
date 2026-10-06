from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    id: int
    title: str
    description: str
    due_date: date
