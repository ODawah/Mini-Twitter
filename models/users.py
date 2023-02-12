from dataclasses import dataclass


# class of interaction with tweets
@dataclass
class User:
    name: str
    email: str
    password: str
    uuid: str = ""

