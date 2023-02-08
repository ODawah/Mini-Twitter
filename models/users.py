from dataclasses import dataclass

# class of interaction with tweets
@dataclass
class User:
    uuid: int
    name: str
    email: str
    password: str