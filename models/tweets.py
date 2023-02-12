from dataclasses import dataclass
from datetime import datetime


# class of interaction with tweets
@dataclass
class Tweet:
    user_uuid: str
    text: str
    is_deleted: bool
    is_reply: bool
    uuid: str = ""
    created_at: datetime = None
