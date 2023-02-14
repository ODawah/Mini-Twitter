from dataclasses import dataclass
from datetime import datetime


# class of interaction with tweets
@dataclass
class Tweet:
    user_uuid: str
    text: str
    uuid: str = ""
    created_at: datetime = None
    is_deleted: bool = False
    is_reply: bool = False
