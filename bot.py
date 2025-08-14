import logging
from telegram.ext import Updater, CommandHandler, MessageHandler
from config import TOKEN

logging.basicConfig(level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! I\'m AYOMIKUN-MD')

def tagall(update, context):
                             
    pass

def makeadmin(update, context):
                        
    pass

def adduser(update, context):
                      
    pass

def kick(update, context):
                       
    pass

def mute(update, context):
                          
    pass

def ban(update, context):
                      
    pass

def block(update, context):
                        
    pass

def unblock(update, context):
                          
    pass

def creategroup(update, context):
                          
    pass

def generate_image(update, context):
                            
    pass

def fun(update, context):
                              
    pass

def games(update, context):
                                
    pass

def motivation(update, context):
                                        
    pass

def advice(update, context):
                            
    pass

def download(update, context):
                                     
    pass

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('def tagall(update, context):
    # code to tag all members
    pass

def makeadmin(update, context):
    # code to make admin
    pass

def adduser(update, context):
    # code to add user
    pass

def kick(update, context):
    # code to kick user
    pass

def mute(update, context):
    # code to mute channel
    pass

def ban(update, context):
    # code to ban user
    pass

def block(update, context):
    # code to block user
    pass

def unblock(update, context):
    # code to unblock user
    pass

def creategroup(update, context):
    # code to create group
    pass

def generate_image(update, context):
    # code to generate image
    pass

def fun(update, context):
    # code to display fun menu
    pass

def games(update, context):
    # code to display games menu
    pass

def motivation(update, context):
    # code to display motivational quote
    pass

def advice(update, context):
    # code to provide advice
    pass

def download(update, context):
    # code to download photo or video
    pass

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('tagall', tagall))
    dp.add_handler(CommandHandler('makeadmin', makeadmin))
    dp.add_handler(CommandHandler('adduser', adduser))
    dp.add_handler(CommandHandler('kick', kick))
    dp.add_handler(CommandHandler('mute', mute))
    dp.add_handler(CommandHandler('ban', ban))
    dp.add_handler(CommandHandler('block', block))
    dp.add_handler(CommandHandler('unblock', unblock))
    dp.add_handler(CommandHandler('creategroup', creategroup))
    dp.add_handler(CommandHandler('generate_image', generate_image))
    dp.add_handler(CommandHandler('fun', fun))
    dp.add_handler(CommandHandler('games', games))
    dp.add_handler(CommandHandler('motivation', motivation))
    dp.add_handler(CommandHandler('advice', advice))
    dp.add_handler(CommandHandler('download', download))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()