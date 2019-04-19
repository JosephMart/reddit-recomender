import json
from typing import Dict, Union, Type

class Subreddit:
    _id: int = None
    subscribers: int = None
    title: str = None
    description: str = None
    over_18: bool = None
    display_name: str = None

    @staticmethod
    def from_json(j: Dict[str, Union[str, int]]):
        s = Subreddit()
        s._id = j["id"]
        s.display_name = j["display_name"][0]
        try:
            s.description = j["public_description"][0]
        except:
            s.description = ""
        s.title = j["title"][0]
        s.subscribers = j["subscribers"][0]
        s.over_18 = j["over18"][0]

        return s

    def to_json(self):
        return {
            "id": self._id,
            "display_name": self.display_name
            "subscribers": self.subscribers,
            "title": self.title,
            "description": self.description,
            "over18": self.over_18
        }
