import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@murad_ai_vip"
LINK = "https://t.me/murad_ai_vip"

async def check_sub(uid, ctx):
    try:
        m = await ctx.bot.get_chat_member(CHANNEL, uid)
        return m.status in ['member','administrator','creator']
    except:
        return False

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton("📢 اشترك في @murad_ai_vip", url=LINK)],
          [InlineKeyboardButton("✅ تحقق من الاشتراك", callback_data="chk")]]
    await update.message.reply_text(f"مرحبا يا {update.effective_user.first_name}! بوت ادوات مراد 🤖\n\n👇 اشترك اولا:", reply_markup=InlineKeyboardMarkup(kb))

async def btn(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if await check_sub(q.from_user.id, ctx):
        kb = [[InlineKeyboardButton("🎨 مولد صور", callback_data="img")],
              [InlineKeyboardButton("🌍 مترجم", callback_data="tr")],
              [InlineKeyboardButton("✍️ كاتب محتوى", callback_data="wr")]]
        await q.edit_message_text("✅ تم التفعيل! اختر:", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await q.edit_message_text(f"❌ لم تشترك بعد!\n{LINK}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✅ تحقق", callback_data="chk")]]))

async def msg(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🤖 استلمت: {update.message.text}")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(btn))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, msg))
app.run_polling()
