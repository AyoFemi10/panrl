import google
from googlesearch import search

def google_search(update, context):
    query = " ".join(context.args)
    try:
        results = search(query, num_results=5)
        response = "Top 5 results:\n"
        for i, result in enumerate(results):
            response += f"{i+1}. {result}\n"
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Error: {str(e)}")
