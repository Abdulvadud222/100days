# from smtplib import SMTP

# my_email = "abdulvadud715@gmail.com"
# password = "@Bdulvadud22"
# connection = SMTP("smpt.gmail.com")
# connection.starttls() ###this secures the message by encrypting it
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="akhmadkhanovabdulvadud@gmail.com", msg="Hello")
# connection.close()

import asyncio
import telegram
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import random
import schedule
import time

TOKEN = "7845968349:AAHO1eDSnihBDydpVWkjO9oPphjpSh-Yo_o"
ADMIN_ID = 1313250514  # Replace with your Telegram user ID

bot = Bot(token=TOKEN)
user_chat_ids = set()  # Store users who start the bot

# Function to get a random quote
def get_random_quote():
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
    return random.choice(all_quotes).strip()

# Start command
async def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_chat_ids.add(chat_id)  # Store chat ID

    # Get a random motivational quote
    quote = get_random_quote()

    await update.message.reply_text(
        f"Hello {user.first_name}!\n"
        "You need a bit of motivation every day?\nNo problem! "
        "This bot will send you motivational quotes daily 😉\n\n"
        f"🌟 Here's a quote to start: \n\n'{quote}'"
    )

async def send_daily_message():
    """Send a daily motivational quote to all users."""
    quote = get_random_quote()

    for chat_id in user_chat_ids:
        try:
            await bot.send_message(chat_id=chat_id, text=f"🌟 Today's quote: {quote}")
        except Exception as e:
            print(f"Failed to send message to {chat_id}: {e}")

def run_schedule():
    """Keep running scheduled tasks."""
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for a minute before checking again

async def schedule_daily_messages():
    """Schedule the daily quote at 06:00 AM UTC."""
    schedule.every().day.at("06:00").do(lambda: asyncio.create_task(send_daily_message()))
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, run_schedule)

# Echo messages and forward them to the admin
async def echo(update: Update, context: CallbackContext):
    user = update.message.from_user
    message_text = update.message.text
    chat_id = update.message.chat_id

    user_chat_ids.add(chat_id)  # Store chat ID if the user sends a message

    # Forward message to admin
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"📩 Message from {user.first_name} ({user.id}):\n{message_text}"
    )

async def main():
    app = Application.builder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start scheduling in a background task
    asyncio.create_task(schedule_daily_messages())

    # Run the bot
    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())  # Ensure the event loop runs properly




