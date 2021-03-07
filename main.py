import Constans as keys
from telegram.ext import *
import Responses as R
import logging

print("Bot started ...")

def start_command(update, context):
    update.message.reply_text('Type something!')

def help_command(update, context):
    update.message.reply_text('Help!')

def handle_message(update, context):
    text =str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)
    logging.info(f"INPUT: {text} OUTPUT: {response[0:30]}.... ")

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()