import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8987342278:AAHiC6S30VBGJGPO2w14Fc2XcK7Cwci5IHs"

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot @murad_vip_2026_bot is Alive 24/7!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "هلا والله يا بطل! 🔥\n\n"
        "بوت قناة مراد VIP شغال 24 ساعة ✅\n\n"
        "من المكلا - حضرموت 🌍\n"
        "موقعنا: murad-ai-hub-vip.netlify.app\n"
        "مجتمعنا: @murad_ai_community"
    )

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

if __name__ == '__main__':
    Thread(target=run_flask, daemon=True).start()
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot started 24/7...")
    application.run_polling()
