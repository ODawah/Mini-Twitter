from dataclasses import dataclass
from datetime import datetime


# class of interaction with tweets
@dataclass
class Tweet:
    uuid: str
    user_uuid: str
    text: str
    created_at: datetime
    is_deleted: bool
    is_reply: bool
