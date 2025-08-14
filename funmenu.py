import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
]

memes = [
    "https://example.com/meme1.jpg",
    "https://example.com/meme2.jpg",
    "https://example.com/meme3.jpg",
]

def fun(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Fun menu:\n/joke\n/meme")

def joke(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(jokes))

def meme(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=random.choice(memes))