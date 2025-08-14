 from pytube import YouTube
import requests

def download(update, context):
    url = context.args[0]
    if "youtube" in url:
        yt = YouTube(url)
        yt.streams.first().download()
        context.bot.send_video(chat_id=update.effective_chat.id, video=open(yt.title + ".mp4", "rb"))
    else:
        response = requests.get(url)
        if response.status_code == 200:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=response.content)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Failed to download photo/video.")