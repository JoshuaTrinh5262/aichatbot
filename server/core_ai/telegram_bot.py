# pip install python-telegram-bot
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from typing import Final
from chat_gpt import ChatGPT
import dotenv

config = dotenv.dotenv_values("./.env")
teleram_token = config['TELEGRAM_BOT_TOKEN']
teleram_username = config['TELEGRAM_BOT_USERNAME']

print('Starting up bot...')

TOKEN: Final = teleram_token
BOT_USERNAME: Final = teleram_username

chat = ChatGPT()

# Lets us use the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m a bot. What\'s up?')


# Lets us use the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Try typing anything and I will do my best to respond!')

# Lets us use the /custom command
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command, you can add whatever text you want here.')

def handle_response(text: str) -> str:
    # Create your own response logic
    return chat.customBard(text)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return   # We don't want the bot respond if it's not mentioned in the group
    else:
        response: str = handle_response(text)

    # Reply normal if the message is in private
    print('Bot:', response)
    await update.message.reply_text(response)

# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

def telegram_bot():
    bot = Application.builder().token(TOKEN).build()

    # Commands
    bot.add_handler(CommandHandler('start', start_command))
    bot.add_handler(CommandHandler('help', help_command))
    bot.add_handler(CommandHandler('custom', custom_command))

    # Messages
    bot.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    bot.add_error_handler(error)

    print('Polling...')
    # Run the bot
    bot.run_polling(poll_interval = 5)
