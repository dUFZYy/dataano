import uuid
from dataclasses import dataclass
from datetime import datetime

# Inconsistency: using dataclass here but standard classes below
@dataclass
class User:
    id: str
    username: str
    email: str

class Task:
    """Represents a task in the system."""
    
    def __init__(self, title, description=""):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.created_at = datetime.now() # TODO: Should we use UTC?
        self.status = "pending"

    def complete(self):
        self.status = "completed"

    def to_dict(self):
        # Missing error handling if attributes are suddenly missing
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "status": self.status
        }
