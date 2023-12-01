from flask import Flask, request, jsonify
from pymongo import MongoClient
import requests
import os
import urllib.parse

app = Flask(__name__)

# Get MongoDB endpoint
database_host = os.getenv("MONGODB_HOST", "localhost")
database_port = os.getenv("MONGODB_PORT", "27017")
database_user = os.getenv("MONGODB_USER", "mongoadmin")
database_pwd = os.getenv("MONGODB_PWD", "secret")

# MongoDB Configuration
username = urllib.parse.quote_plus(database_user)
password = urllib.parse.quote_plus(database_pwd)
mongo_client = MongoClient(f"mongodb://{username}:{password}@{database_host}:{database_port}/")  # MongoDB connection string
db = mongo_client["dictionary"]  # MongoDB database name
collection = db["wordscollection"]  # MongoDB collection name

# Dictionary API Endpoint
dictionary_api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"  # Dictionary API URL

@app.route('/search', methods=['GET'])
def query():
    query_string = request.args.get('word')

    # Check if the word is in MongoDB
    result = collection.find_one({"word": query_string})
    if result:
        response_data = result['result']
    else:
        # If not found in MongoDB, fetch data from the Dictionary API
        dict_api_response = requests.get(f"{dictionary_api_url}{query_string}")
        response_data = dict_api_response.json()

        # Save the response in MongoDB
        collection.insert_one({"word": query_string, "result": response_data})

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
