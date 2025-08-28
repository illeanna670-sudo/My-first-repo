# bot.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os


TOKEN = 8393611715:AAEmY_I1i7bpnWz_jCsQCK1PP6Drcivm_Gs

# Yaha apne channels daalo
CHANNELS = ["@shadow_studio_fan", "@https://t.me/+qjpi1QXEkZtlOTk1l"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("✅ Verify & Unlock", callback_data="verify")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🚨 Pehle niche diye gaye sabhi channels join karo:\n\n" + 
        "\n".join([f"👉 {c}" for c in CHANNELS]) +
        "\n\nPhir niche button dabao unlock karne ke liye.",
        reply_markup=reply_markup
    )

async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    for channel in CHANNELS:
        member = await context.bot.get_chat_member(channel, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            await query.edit_message_text(
                "❌ Aapne abhi tak sabhi channels join nahi kiye!\nPehle join karke dobara try karo."
            )
            return

    await query.edit_message_text(
        "✅ Verified! Yeh lo aapka episode link:\n👉 https://your-link-here.com"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(verify, pattern="verify"))
    app.run_polling()

if __name__ == "__main__":
    main()
