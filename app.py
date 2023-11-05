import streamlit as st

st.title("Data Science Club - PSUT")
st.header("Welcome to the Data Science Club")

import requests
import json

url = "https://eu-central-1.aws.data.mongodb-api.com/app/data-znkwb/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "<COLLECTION_NAME>",
    "database": "<DATABASE_NAME>",
    "dataSource": "dscdev",
    "projection": {
        "_id": 1
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'YGzf1Lv9D6P3mCVhPH18gJZeDkQTk9fiD7guslq5LvDK7oqC6MMggn5xsNjvZnLn',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = f"mongodb+srv://a_tabaza:{st.secrets['MONGODB_DB_PASSWORD']}@dscdev.ohomzmf.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)