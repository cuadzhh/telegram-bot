import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Xin chào!\n"
        "Bot đang hoạt động.\n\n"
        "Gõ /help để xem các lệnh."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Danh sách lệnh:\n"
        "/start - Khởi động bot\n"
        "/help - Xem hướng dẫn"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bạn vừa gửi: " + update.message.text
    )

def main():
    if not TOKEN:
        raise RuntimeError("Chưa thiết lập BOT_TOKEN")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    )

    print("Bot đang chạy...")
    app.run_polling()

if __name__ == "__main__":
    main()
  
