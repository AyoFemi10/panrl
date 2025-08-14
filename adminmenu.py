blocked_users = []

def block(update, context):
    user_id = context.args[0]
    blocked_users.append(user_id)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"User {user_id} blocked")

def unblock(update, context):
    user_id = context.args[0]
    if user_id in blocked_users:
        blocked_users.remove(user_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"User {user_id} unblocked")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"User {user_id} is not blocked")

def creategroup(update, context):
    group_title = " ".join(context.args)
    context.bot.create_chat(title=group_title, type="group")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Group {group_title} created")