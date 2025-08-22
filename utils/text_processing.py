import vertexai
from vertexai.generative_models import GenerativeModel
import streamlit as st
import json
from google.oauth2 import service_account


service_account_info = dict(st.secrets["google_service_account"])
credentials = service_account.Credentials.from_service_account_info(service_account_info)


PROJECT_ID = st.secrets["PROJECT_ID"]
LOCATION = st.secrets["LOCATION"]


vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)


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

