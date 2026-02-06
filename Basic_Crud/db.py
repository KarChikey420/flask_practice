from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from flask import request

load_dotenv()

app=Flask(__name__)

client= MongoClient(os.getenv('mongo_link'))
db=client("my_database")
collection=db['user1']

model={
    'user_name':str,
    'password':str,
    'scored':int,
    'class':str
}

@app.route('/users',method=['POST'])
def create():
    data=request.get_json()
    collection.insert_one(model.get(data))
