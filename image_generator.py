import torch
from diffusers import StableDiffusionPipeline

# Stable Diffusion model for image generation
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

def generate_image(prompt):
    image = pipe(prompt).images[0]
    return image
from diffusers import StableDiffusionPipeline
import torch

model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

def generate_image(update, context):
    prompt = " ".join(context.args)
    image = pipe(prompt).images[0]
    image.save("image.png")
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open("image.png", "rb"))