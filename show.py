import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://bbhcca21020:qQ1XnGQ9XmOZZCVQ@cluster0.qzlwovv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.message_board_db
collection = db.messages

# Set up the page title
st.title("Anonymous Message Board - Display Messages")

# Function to load messages from MongoDB
def load_messages():
    messages = collection.find({})
    return [msg["message"] for msg in messages]

# Load and display all messages
messages = load_messages()
if messages:
    st.write("### Messages")
    for msg in messages:
        st.write(f"- {msg}")
else:
    st.write("No messages have been submitted yet.")
