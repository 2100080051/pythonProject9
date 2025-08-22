from vertexai.vision_models import ImageGenerationModel
from PIL import Image

image_model = ImageGenerationModel.from_pretrained("imagegeneration@005")

def generate_image(prompt, path):
    """Generate storybook illustration from text chunk with fallback prompts."""
    try:
        images = image_model.generate_images(prompt=prompt)
        if images and images[0]:
            images[0].save(path)
            return path
        else:
            print("⚠️ No image returned for:", prompt)
            # Fallback retry
            fallback_prompt = f"{prompt}. Storybook style, colorful, cartoon, child-friendly illustration."
            print("🔄 Retrying with fallback prompt:", fallback_prompt)
            images = image_model.generate_images(prompt=fallback_prompt)
            if images and images[0]:
                images[0].save(path)
                return path
            else:
                print("⚠️ Even fallback failed.")
                return None
    except Exception as e:
        print("❌ Image generation error:", e)
        return None
