from dataclasses import dataclass
from datetime import datetime


# class of interaction with tweets
@dataclass
class Tweet:
    uuid: int
    user_uuid: int
    text: str
    created_at: datetime
    is_deleted: bool
    is_reply: bool