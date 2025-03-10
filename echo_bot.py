# Import necessary libraries
import telebot  # 📦 Library to create Telegram bots
import logging  # 📜 Library for logging messages to the terminal

# Set up logging to display info in the terminal
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',  # 🕒 Format: Timestamp - Level - Message
    level=logging.INFO  # ✅ Show INFO level messages and above
)

# Initialize the bot with your provided Bot Token
# 🔑 Token: 8063661813:AAEyg7FN7rGccYDwHf0UmI3aWMY6dQfZqH0
bot = telebot.TeleBot('Enter your bot father token')

# Handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # 🎉 Welcome message with proper Markdown formatting
    welcome_msg = "👋 *Hello! I’m your Echo Bot!* 🤖\nSend me any message, and I’ll echo it back with some style! ✨"
    bot.send_message(message.chat.id, welcome_msg, parse_mode='Markdown')
    # 📜 Log the action in the terminal
    logging.info(f"Sent welcome message to {message.from_user.username} (ID: {message.from_user.id})")

# Handler for the /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    # ℹ️ Help message with proper Markdown formatting
    help_msg = "📋 *How to Use Me:*\n- Just type anything, and I’ll repeat it with bold text and emojis!\n- Try commands like /start or /help."
    bot.send_message(message.chat.id, help_msg, parse_mode='Markdown')
    # 📜 Log the action in the terminal
    logging.info(f"Sent help message to {message.from_user.username} (ID: {message.from_user.id})")

# Handler for all text messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    user_text = message.text  # 📥 Get the user’s input
    if user_text.startswith('/'):
        # 🚫 Handle commands separately to avoid echoing them
        error_msg = "❓ *Oops!* I only echo regular messages. Try something without a slash!"
        bot.send_message(message.chat.id, error_msg, parse_mode='Markdown')
        logging.info(f"User {message.from_user.username} sent a command: {user_text}")
    else:
        # 🎨 Echo the message with proper Markdown formatting
        echoed_text = f"📢 *You said:* {user_text}\n🔄 *Echoing back:* *{user_text.upper()}* 🎉"
        bot.send_message(message.chat.id, echoed_text, parse_mode='Markdown')
        # 📜 Log the echoed message in the terminal
        logging.info(f"Echoed '{user_text}' back to {message.from_user.username} (ID: {message.from_user.id})")

# 🚀 Start the bot and keep it running
logging.info("🚀 Bot is starting...")
bot.polling()
