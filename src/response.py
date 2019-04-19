import json
from typing import Dict, Union, Type

class Subreddit:
    _id: int = None
    subscribers: int = None
    title: str = None
    description: str = None
    over_18: bool = None

    @staticmethod
    def from_json(j: Dict[str, Union[str, int]]):
        s = Subreddit()
        s._id = j["id"]
        s.description = j["public_description"][0]
        s.title = j["title"][0]
        s.subscribers = j["subscribers"][0]
        s.over_18 = j["over18"][0]

        return s

    def to_json(self):
        return {
            "id": self._id,
            "subscribers": self.subscribers,
            "title": self.title,
            "description": self.description,
        }

# class Response:
#     num_found: int = None
#     start: int = None
#     subreddits: List[Subreddit] = []

    # def from_solr_response(j: Dict[str, Union[str, int]]) -> Res
