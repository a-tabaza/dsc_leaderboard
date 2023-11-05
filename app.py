import streamlit as st
import pandas as pd

st.title("Data Science Club - PSUT")
st.header("Welcome to the Data Science Club")

# import requests
# import json

# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = f"mongodb+srv://a_tabaza:{st.secrets['MONGODB_DB_PASSWORD']}@dscdev.ohomzmf.mongodb.net/?retryWrites=true&w=majority"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

# db = client.leaderboard
# users = db.users

# # data = users.find_one({'username': 'Abdulrahman Tabaza'})

# for user in users.find():
#     st.write(user['username'])
#     st.write(user['score'])

names = ['Abdulrahman Tabaza', 'Mohammad Doleh']
scores = [100, 200]

df = pd.DataFrame({'Name': names, 'Score': scores})
df = df.sort_values(by='Score', ascending=False)
st.dataframe(df)

# #for user in data:
# st.write(data['username'])