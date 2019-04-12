from flask import Flask, request, jsonify
import solr

app = Flask(__name__)

@app.route('/search', methods = ['POST'])
def search():
    data = request.form # a multidict containing POST data
    print(data)
    data_json = request.get_json()
    print(data_json)
    solr.search()

    return jsonify(data_json)

app.run(port=8080)
