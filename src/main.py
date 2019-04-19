from flask import Flask, request, jsonify
from flask_cors import CORS
from typing import List
from response import Subreddit
import solr
import utils
import traceback

app = Flask(__name__)
CORS(app)

@app.route("/search", methods=["POST"])
def search():
    body = request.get_json()

    query_subs: List[Subreddit] = None
    try:
        query_subs = solr.validate_query(body["subreddits"])
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": str(e)}), 400
    query_words, query_words_lmtzd = utils.analyze_queries(query_subs)

    doc_subs: List[Subreddit] = None
    doc_subs = solr.get_docs(query_words)
    docs_lmtzd = utils.analyze_documents(doc_subs)

    result = utils.order(query_words_lmtzd, docs_lmtzd, doc_subs)

    return jsonify({"result": list(result)})

@app.route("/autocomplete", methods=["GET"])
def autocomplete():
    q = request.args.get("q")
    over18 = request.args.get("over18")
    results = solr.autocomplete(q, over18)
    return jsonify({"results": results})

app.run(port=8080)

# query1 = "JavaScript is for losers who like web development"
# query2 = "JavaScript is good for front end web development"

# docs = [
#     "JavaScript is a great language",
#     "I really enjoy writing JavaScript on the front end",
#     "Modern web development is done using JavaScript"
# ]

# doc_ids = [1, 2, 3]

# analyzed_query = utils.analyze_queries([query1, query2])
# analyzed_docs = utils.analyze_documents(docs)
# result = utils.order(analyzed_query, analyzed_docs, doc_ids)

# print(result)

# solr.search(set(["basketball", "baseball"]))
