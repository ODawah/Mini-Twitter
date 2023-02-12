from dataclasses import dataclass


# class of interaction with tweets
@dataclass
class User:
    uuid: str
    name: str
    email: str
    password: str
