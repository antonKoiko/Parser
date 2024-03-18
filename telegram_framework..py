import signal
import sys
import time
import telebot
from tg import BOT_TOKEN, chat_id

# Replace with your actual Telegram bot token (obtain from BotFather)


bot = telebot.TeleBot(BOT_TOKEN)
pause_time = 5

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to_message(message, f"Hi! I'll announce the current time every {pause_time} seconds.")

def announce_time():
    while True:
        current_time = time.strftime(f" Текущее время: %Hч.%Mм.%Sс."
                                     f"\nСледующее обновление через {pause_time} секунд", time.localtime())
        bot.send_message(chat_id, current_time)  # Replace with the chat ID where you want the bot to send messages
        time.sleep(pause_time)

if __name__ == "__main__":

    announce_time()
    bot.polling()
