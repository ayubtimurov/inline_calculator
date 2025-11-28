from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Application, InlineQueryHandler, ContextTypes, CommandHandler
import uuid
import re
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Start command recieved")
    await update.message.reply_text("You started Inline Calculator Bot in Telegram!")

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("About command recieved")
    text = "This is an Inline Calculator Bot in Telegram. Type an expression to calculate e.g.(5+4)"
    await update.message.reply_text(text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Help command recieved")
    help_text = """
    📱 *Inline Calculator*
/start - Start the bot
/about - About the bot
/help - Show this message
"""
    await update.message.reply_text(help_text)

# Calculations
def safe_calculate(expression: str):

    expression = expression.replace(" ", "")

    if not re.match(r"^[\d+\-\*\/\(\)\.]+$", expression):
        raise ValueError("Invalid charachters")
    return eval(expression)
    
async def inline_calculator(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query

    if not query:
        return
    
    try:
        result = safe_calculate(query)

        results = [
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title=f"= {result}",
                input_message_content=InputTextMessageContent(
                    message_text=f"<code>{query}</code> = <b>{result}</b>",
                    parse_mode='HTML'
                ),
                description=f"{query} equals to {result}",
                thumbnail_url="https://via.placeholder.com/64/0088cc/ffffff?text"
            )
        ]
        await update.inline_query.answer(results, cache_time=1)

    except Exception as e:
        results = [
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="Invalid Expression",
                input_message_content=InputTextMessageContent(
                    message_text="Cannot calculate this expression"
                ),
                description="Please chech your calculation"
            )
        ]
        await update.inline_query.answer(results, cache_time=1)


if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("help", help_command))

    # Error
    app.add_handler(InlineQueryHandler(inline_calculator))

    print("Polling...")
    app.run_polling()
