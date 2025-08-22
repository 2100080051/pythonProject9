import streamlit as st
from utils.text_processing import generate_story, split_into_chunks
from utils.image_generation import generate_image
from utils.pdf_export import export_storybook
import os

st.title("📚 AI Storybook Generator (Google Gemini + Imagen)")

sample_concepts = [
    "A little red dragon learning to fly",
    "A rabbit and a turtle becoming friends in the forest",
    "A robot who wants to learn painting",
    "A spaceship full of cats traveling to the moon",
    "A magical tree that tells bedtime stories"
]

concept = st.text_input("Enter story concept:", sample_concepts[0])
if st.button("🎲 Random Sample"):
    import random
    concept = random.choice(sample_concepts)
    st.session_state['concept'] = concept
    st.experimental_rerun()

language = st.selectbox("Language:", ["English", "Hindi", "Telugu", "French", "Spanish"])
generate_btn = st.button("Generate Storybook")

if generate_btn:
    with st.spinner("✨ Generating story..."):
        story = generate_story(concept, language)
        chunks = split_into_chunks(story, max_words=60)

        content = []  
        os.makedirs("static", exist_ok=True)

        for idx, chunk in enumerate(chunks):
            st.subheader(f"📖 Page {idx+1}")
            st.write(chunk)
            img_path = f"static/page_{idx+1}.png"
            st.write(f"🎨 Generating illustration for page {idx+1}...")
            image_path = generate_image(f"Storybook illustration: {chunk}", img_path)
            if image_path:
                st.image(image_path, caption=f"Page {idx+1} Illustration")
            content.append((chunk, image_path))

        export_storybook([c for c, _ in content], [i for _, i in content], "storybook.pdf", concept=concept)
        st.success("✅ Storybook created!")
        st.download_button("📥 Download PDF", open("storybook.pdf", "rb"), "storybook.pdf")


