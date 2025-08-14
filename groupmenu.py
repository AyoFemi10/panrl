def tagall(update, context):
    chat_id = update.effective_chat.id
    members = context.bot.get_chat_members(chat_id)
    member_ids = [member.user.id for member in members]
    mentions = [f"[{member.user.first_name}](tg://user?id={member.user.id})" for member in members]
    context.bot.send_message(chat_id=chat_id, text=" ".join(mentions), parse_mode="Markdown")

def makeadmin(update, context):
    chat_id = update.effective_chat.id
    user_id = context.args[0]
    context.bot.promote_chat_member(chat_id=chat_id, user_id=user_id, can_change_info=True, can_delete_messages=True, can_invite_users=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True)

def adduser(update, context):
    chat_id = update.effective_chat.id
    user_id = context.args[0]
    context.bot.add_chat_member(chat_id=chat_id, user_id=user_id)

def kick(update, context):
    chat_id = update.effective_chat.id
    user_id = context.args[0]
    context.bot.kick_chat_member(chat_id=chat_id, user_id=user_id)

def mute(update, context):
    chat_id = update.effective_chat.id
    context.bot.set_chat_permissions(chat_id=chat_id, permissions=ChatPermissions(can_send_messages=False))

def ban(update, context):
    chat_id = update.effective_chat.id
    user_id = context.args[0]
    context.bot.ban_chat_member(chat_id=chat_id, user_id=user_id)
    