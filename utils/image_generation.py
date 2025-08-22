from vertexai.vision_models import ImageGenerationModel
from PIL import Image

# Lazy-load the model only when needed
_image_model = None

def generate_image(prompt, path):
    """Generate storybook illustration from text chunk with fallback prompts."""
    global _image_model
    if _image_model is None:
        # Initialize the model only once, after credentials are set
        _image_model = ImageGenerationModel.from_pretrained("imagegeneration@005")

    try:
        images = _image_model.generate_images(prompt=prompt)
        if images and images[0]:
            images[0].save(path)
            return path
        else:
            print("⚠️ No image returned for:", prompt)
            # Fallback retry with a more descriptive style
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
