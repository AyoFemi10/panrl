# ai.py

import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def ask_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use GPT-4 if your key allows it
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"❌ Error: {e}"
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from chatterbot import ChatBot

# Transformers model for conversational AI
tokenizer = AutoTokenizer.from_pretrained("t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")

def generate_response(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Chatterbot for simple chat responses
chatbot = ChatBot("AYOMIKUN-MD")

def get_chat_response(input_text):
    response = chatbot.get_response(input_text)
    return response