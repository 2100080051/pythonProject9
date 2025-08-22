import vertexai
from vertexai.generative_models import GenerativeModel
import streamlit as st
import os, json

# Convert st.secrets entry to a dict and save as JSON file
service_account_info = dict(st.secrets["google_service_account"])
with open("gcp_key.json", "w") as f:
    json.dump(service_account_info, f)

# Point Google SDK to this key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_key.json"

# Load project details from secrets
PROJECT_ID = st.secrets["PROJECT_ID"]
LOCATION = st.secrets["LOCATION"]

# Initialize Vertex AI
vertexai.init(project=PROJECT_ID, location=LOCATION)

# Load Gemini model
model = GenerativeModel("gemini-2.0-flash")


def generate_story(concept: str, language: str = "English", max_words=500):
    """Generate a story based on a concept and language"""
    prompt = f"Write a story in {language} for children about: {concept}. Make it easy, fun, and storybook-like."
    response = model.generate_content(prompt)
    return response.text


def split_into_chunks(text, max_words=60):
    """Split story into smaller chunks (pages)."""
    words = text.split()
    return [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]
