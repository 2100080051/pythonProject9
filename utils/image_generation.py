from vertexai.vision_models import ImageGenerationModel
from PIL import Image
import streamlit as st
from google.oauth2 import service_account
import vertexai
import json


_image_model = None

def _init_vertex_ai():
    """Initialize Vertex AI with credentials from Streamlit secrets"""
    service_account_info = dict(st.secrets["google_service_account"])
    credentials = service_account.Credentials.from_service_account_info(service_account_info)

    PROJECT_ID = st.secrets["PROJECT_ID"]
    LOCATION = st.secrets["LOCATION"]

    vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)


def generate_image(prompt, path):
    """Generate storybook illustration from text chunk with fallback prompts."""
    global _image_model
    if _image_model is None:
        _init_vertex_ai()
        _image_model = ImageGenerationModel.from_pretrained("imagegeneration@005")

    try:
        images = _image_model.generate_images(prompt=prompt)
        if images and images[0]:
            images[0].save(path)
            return path
        else:
            print("⚠️ No image returned for:", prompt)
            
            fallback_prompt = f"{prompt}. Storybook style, colorful, cartoon, child-friendly illustration."
            print("🔄 Retrying with fallback prompt:", fallback_prompt)
            images = _image_model.generate_images(prompt=fallback_prompt)
            if images and images[0]:
                images[0].save(path)
                return path
            else:
                print("⚠️ Even fallback failed.")
                return None
    except Exception as e:
        print("❌ Image generation error:", e)
        return None

