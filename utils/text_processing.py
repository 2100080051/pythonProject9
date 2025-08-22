import vertexai
from vertexai.generative_models import GenerativeModel

PROJECT_ID = "my-project-8-465221"
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

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
