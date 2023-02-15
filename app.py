import os
import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
				   text='Я бот для поддержки курса "Анализ данных в индустрии". '
				  	+ 'Для выполнения ДЗ вам потребуется <code>chat_id</code>. '
				        + f'Ваш <code>chat_id</code> равен {update.effective_chat.id}.')

async def get_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
				   text=update.effective_chat.id)

if __name__ == "__main__":
    token = os.getenv("TELEGRAM_TOKEN")
    application = ApplicationBuilder().token(token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("get_chat", get_chat))
    
    application.run_polling()
