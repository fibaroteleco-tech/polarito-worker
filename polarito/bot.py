import asyncio
from telegram import Bot
from telegram.ext import ApplicationBuilder, MessageHandler, filters

TOKEN = "8165829493:AAEMajVQ4C8XQ-f4NLrf3xNwxJ6JrTLnNVg"

async def start_bot():
    bot = Bot(token=TOKEN)

    app = ApplicationBuilder().token(TOKEN).build()

    async def echo(update, context):
        await update.message.reply_text("Bot operativo 👌")

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot iniciado y funcionando 🔥")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(start_bot())
