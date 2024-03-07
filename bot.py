from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

# Use your Bot Token here
TOKEN = '1953339762:AAHBpdwL9YIExZCY1A1uxY_zoZf5H2acqes' #1953339762:AAHBpdwL9YIExZCY1A1uxY_zoZf5H2acqes

# List of USER_IDs of the users whose messages you want to forward
USER_IDS = [937816408, 1182551708]# thomas 937816408 #indigo 1182551708

# TARGET_CHAT_ID is the id of the chat where you want to forward these messages
TARGET_CHAT_ID = -1002085260355 #thomas forwarding channel

async def filter_and_forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if the message is from one of the users you're monitoring
    if update.message.from_user.id in USER_IDS:
        print(f'message from user {update.message.from_user.id}')
        # Forward the message to the target chat
        await context.bot.forward_message(chat_id=TARGET_CHAT_ID,
                                        from_chat_id=update.message.chat_id,
                                        message_id=update.message.message_id)

def main():
    application = Application.builder().token(TOKEN).build()

    # Using the non-command message handler
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, filter_and_forward)
    application.add_handler(message_handler)

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
