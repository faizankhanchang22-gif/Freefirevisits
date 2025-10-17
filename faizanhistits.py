import telebot
import requests

# === Configuration ===
BOT_TOKEN = "8399070588:AAGcmo7IhRBlwx-vkER7BIm9m8oYOAv6HEM"  # Tera bot token
OWNER_ID = 6967754590  # Tera Telegram ID
GROUP_ID = -1003089918721  # Tera group ID

# === API ===
API_URL = "http://217.154.239.23:13564/visit?uid=760840390"

bot = telebot.TeleBot(BOT_TOKEN)

# === Access Control ===
def is_owner(user_id):
    return user_id == OWNER_ID

def is_group(chat_id):
    return chat_id == GROUP_ID

# === Commands ===
@bot.message_handler(commands=['start'])
def start_cmd(message):
    if not is_group(message.chat.id):
        bot.reply_to(message, "⚠️ Ye bot sirf owner ke group me hi kaam karta hai.")
        return

    if is_owner(message.from_user.id):
        bot.reply_to(message, "✅ Free Fire Visit Bot ready hai boss!")
    else:
        bot.reply_to(message, "❌ Ye bot sirf owner ke liye restricted hai.")

@bot.message_handler(commands=['visit'])
def visit_cmd(message):
    if not is_group(message.chat.id):
        return

    if not is_owner(message.from_user.id):
        bot.reply_to(message, "🚫 Sirf owner is command ka use kar sakta hai.")
        return

    try:
        r = requests.get(API_URL, timeout=10)
        if r.status_code == 200:
            bot.reply_to(message, f"✅ Visit Request Sent Successfully!\n\nResponse:\n`{r.text}`", parse_mode="Markdown")
        else:
            bot.reply_to(message, f"⚠️ API Error: {r.status_code}")
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

# === Run Bot ===
print("🔥 Free Fire Visit Bot Running... (Only owner & group access)")
bot.polling(non_stop=True)