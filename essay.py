import random

def essay(update, context):
    topic = " ".join(context.args)
    essay_topics = {
        "environment": "The environment is a vital component of our planet. We must take care of it.",
        "technology": "Technology has revolutionized the way we live. It has made our lives easier and more convenient.",
        "education": "Education is the key to success. It opens doors to new opportunities and helps us grow as individuals.",
    }
    if topic.lower() in essay_topics:
        context.bot.send_message(chat_id=update.effective_chat.id, text=essay_topics[topic.lower()])
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, no essay available on that topic.")
        # You can also use a more advanced AI model to generate essays on any topic