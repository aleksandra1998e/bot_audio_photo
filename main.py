import os

import telebot
from telebot import types

from audio import convert_to_wav
from database import save_to_database_audio, save_to_database_photo
from photo import has_face

# Initialize the bot
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)


# Define a function to handle audio messages
@bot.message_handler(content_types=["audio"])
def handle_audio(message: types.Message):
    # Get the audio message and the user ID
    audio = message.audio
    user_id = message.from_user.id

    wav_audio = convert_to_wav(audio)

    # Save the audio file to the database or disk
    # Replace this with the appropriate code for your DBMS or file storage system
    save_to_database_audio(user_id, wav_audio)


@bot.message_handler(content_types=["photo"])
def handle_photo(message: types.Message):
    # Get the photo and the user ID
    photo = message.photo
    user_id = message.from_user.id

    # Check if the photo has a face
    if has_face(photo):
        # Save the photo to the database or disk
        # Replace this with the appropriate code for your DBMS or file storage system
        save_to_database_photo(user_id, photo)


if __name__ == "__main__":
    bot.polling(none_stop=True)
