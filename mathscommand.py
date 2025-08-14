def math(update, context):
    expression = " ".join(context.args)
    try:
        result = eval(expression)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Result: {result}")
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Error: {str(e)}")
import sympy

def math(update, context):
    expression = " ".join(context.args)
    try:
        result = sympy.sympify(expression).evalf()
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Result: {result}")
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Error: {str(e)}")