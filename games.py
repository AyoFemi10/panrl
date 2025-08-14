def games(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Games menu:\n/tictactoe\n/wcg")

def tictactoe(update, context):
    # Tic-Tac-Toe game logic
    board = [" " for _ in range(9)]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Tic-Tac-Toe game started!")
    # ... (rest of the game logic)

def wcg(update, context):
    # Word Chain Game logic
    context.bot.send_message(chat_id=update.effective_chat.id, text="Word Chain Game started!")
    # ... (rest of the game logic)