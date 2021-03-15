from telegram.ext import *
import Responses as R
import logging

import os
from os import environ

API_KEY = environ['TELEGRAM_API_KEY'] 

print("Bot started ...")

def start_command(update, context):
    update.message.reply_text("Navigation: \n /allgemein \n /nord \n /sued \n /foehn \n")

def help_command(update, context):
    update.message.reply_text('Für den DHV Wetterbericht: \n /allgemein \n /nord \n /sued \n')

def handle_message(update, context):
    text =str(update.message.text).lower()
    #response = R.sample_responses(text)
    #update.message.reply_text(response)

    messageType, response = R.sample_responses(text)
    
    if messageType == "txt":
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    elif messageType == "img":
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(response, "rb"))

    logging.info(f"INPUT: {text} OUTPUT: {response[0:30]}.... ")

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()