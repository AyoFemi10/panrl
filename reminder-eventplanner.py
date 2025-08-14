import datetime

events = {}

def event(update, context):
    args = context.args
    if len(args) >= 3:
        event_name = args[0]
        date = args[1]
        time = args[2]
        events[event_name] = {"date": date, "time": time}
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Event '{event_name}' set for {date} at {time}")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid format. Use /event <event_name> <date> <time>")

def reminder(context):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    for event_name, event_details in events.items():
        if event_details["date"] == current_time.split(" ")[0] and event_details["time"] == current_time.split(" ")[1]:
            context.bot.send_message(chat_id=context.job.context, text=f"Reminder: {event_name}")

def start_reminder(update, context):
    context.job_queue.run_repeating(reminder, interval=60, first=0, context=update.effective_chat.id)