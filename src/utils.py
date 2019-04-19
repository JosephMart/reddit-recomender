import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from typing import List, Set
from response import Subreddit

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))

lmtzr = WordNetLemmatizer()

def analyze_queries(subreddits: List[Subreddit]) -> (Set[str], Set[str]):
    words = set()
    lmtzd = set()

    for sub in subreddits:
        tokens = word_tokenize(sub.description)
        non_stop_words = [token.lower() for token in tokens if token not in stop_words]
        words.update(non_stop_words)
        analyzed = [lmtzr.lemmatize(word) for word in non_stop_words]
        lmtzd.update(set(analyzed))

    return non_stop_words, lmtzd

def analyze_documents(subreddits: List[Subreddit]) -> List[Set[str]]:
    docs_lmtzd = []

    for sub in subreddits:
        tokens = word_tokenize(sub.description)
        docs_lmtzd.append(set([lmtzr.lemmatize(word.lower()) for word in tokens if word not in stop_words]))

    return docs_lmtzd

def order(query_lmtzd: Set[str], documents_lmtzd: List[Set[str]], documents: List[Subreddit]) -> List[dict]:
    result = sorted(zip(documents_lmtzd, documents), key=lambda x: len(x[0] & query_lmtzd), reverse=True)

    return [x[1].to_json() for x in result]
