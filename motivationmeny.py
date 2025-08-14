import random

motivational_quotes = [
    "Believe you can and you're halfway there.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
]

advice_topics = {
    "life": "Life is a journey, not a destination. Enjoy the ride.",
    "love": "Love yourself first and everything else will fall into line.",
    "career": "Choose a job you love, and you will never have to work a day in your life.",
}

def motivation(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(motivational_quotes))

def advice(update, context):
    topic = " ".join(context.args)
    if topic in advice_topics:
        context.bot.send_message(chat_id=update.effective_chat.id, text=advice_topics[topic])
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, no advice available for that topic.")