import os
import requests
from typing import Set, List
from response import Subreddit

URL = os.getenv("SOLR_SERVER")
CORE_NAME = os.getenv("CORE_NAME")

SERVER = f"{URL}/solr/{CORE_NAME}/select"

def autocomplete(query: str, over18: bool=False) -> List[dict]:
    params = {
        "q": f"display_name:*{query}* AND over18:{str(over18).lower()}",
        "sort": "subscribers desc",
        "rows": 10
    }

    r = requests.get(SERVER, params)
    body = r.json()

    return [doc["display_name"] for doc in body["response"]["docs"]]

# returns a list of subreddits from the query that don't exist
def validate_query(subreddits: List[str]) -> List[Subreddit]:
    params = {
        "q": " OR ".join(f'display_name:{sub}' for sub in subreddits),
        "rows": len(subreddits)
    }

    r = requests.get(SERVER, params)
    body = r.json()

    if body["response"]["numFound"] != len(subreddits):
        print("error")
        s: List[str] = []
        for doc in body["response"]["docs"]:
            s.append(doc["display_name"])

        not_found =  set(subreddits).symmetric_difference(set(s))
        raise Exception(f"Subreddit(s) not found: {', '.join(f for f in not_found)}")

    subs: List[Subreddit] = []
    for doc in body["response"]["docs"]:
        subs.append(Subreddit.from_json(doc))

    return subs

# returns (display_names, public description)
def get_docs(words: Set[str]) -> List[Subreddit]:
    params = {
        "q": " OR ".join(f'public_description:"{word}" OR title:*{word}* OR display_name:*{word}*' for word in words),
        "rows": 15,
        "sort": "subscribers desc"
    }

    r = requests.get(SERVER, params)
    body = r.json()

    subreddits: List[Subreddit] = []
    if "response" in body:
        for doc in body["response"]["docs"]:
            subreddits.append(Subreddit.from_json(doc))

    return subreddits
