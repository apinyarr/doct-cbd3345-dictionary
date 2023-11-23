from flask import Flask, request, jsonify
from pymongo import MongoClient
import requests
import os

app = Flask(__name__)

# Get MongoDB endpoint
database_host = os.getenv("MONGODB_HOST", "localhost")
database_port = os.getenv("MONGODB_PORT", "27017")
database_user = os.getenv("MONGODB_USER", "mongoadmin")
database_pwd = os.getenv("MONGODB_PWD", "secret")

# MongoDB Configuration
mongo_client = MongoClient(f"mongodb://{database_user}:{database_pwd}@{database_host}:{database_port}/")  # MongoDB connection string
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
    app.run(host='0.0.0.0', port=8088)
