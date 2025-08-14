def ping(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Pong!")
time

start_time = time.time()

def runtime(update, context):
    runtime = time.time() - start_time
    hours = int(runtime // 3600)
    minutes = int((runtime % 3600) // 60)
    seconds = int(runtime % 60)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Runtime: {hours}h {minutes}m {seconds}s")
def users(update, context):
    chat_id = update.effective_chat.id
    members = context.bot.get_chat_members(chat_id)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Users: {len(members)}")
def panel(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Control Panel:\n/ping\n/runtime\n/users\n/adduser")
dp.add_handler(CommandHandler('alive', ping))
