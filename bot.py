from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# 🔑 Replace with your bot token from BotFather
TOKEN = "8433331462:AAHMANRb3gNwW2RhjO-lv4_HnK_GZux_Z_A"

# --- Command functions ---

def start(update, context):
    keyboard = [
        ["📊 Signals", "📈 Market"],
        ["📘 Strategy", "🤝 Refer"],
        ["❓ Help", "📩 Contact"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    update.message.reply_text(
        "👋 Welcome to ForexCapital Bot!\n\n"
        "📊 Daily Forex & Crypto Signals\n"
        "📈 Market Insights & News Updates\n"
        "💹 Smart Trading Strategies\n"
        "🛡 Risk Management Tips\n"
        "🤝 Easy Referral & Rewards\n\n"
        "🚀 Use the menu below to get started!",
        reply_markup=reply_markup
    )

def help_command(update, context):
    update.message.reply_text(
        "Here are the available commands:\n\n"
        "/start - Show welcome message\n"
        "/help - Show this help menu\n"
        "/signals - View today’s forex & crypto signals\n"
        "/market - Get live market updates\n"
        "/strategy - Learn trading strategies\n"
        "/refer - Get your referral link\n"
        "/contact - Contact support"
    )

def signals(update, context):
    update.message.reply_text(
        "📊 Today’s Signals:\n\n"
        "EUR/USD 👉 Buy @ 1.0650, TP 1.0720, SL 1.0610\n"
        "BTC/USDT 👉 Buy @ 26,500, TP 27,200, SL 26,000\n"
        "ETH/USDT 👉 Buy @ 1,750, TP 1,820, SL 1,720"
    )

def market(update, context):
    update.message.reply_text(
        "📈 Market Update:\n\n"
        "⚡ Bitcoin: $26,780 (+2.3%)\n"
        "⚡ Ethereum: $1,770 (+1.8%)\n"
        "⚡ EUR/USD: 1.0680 (+0.5%)"
    )

def strategy(update, context):
    update.message.reply_text(
        "📘 Trading Strategy Tip:\n\n"
        "✅ Always use stop-loss to manage risk.\n"
        "✅ Risk only 1-2% of your capital per trade.\n"
        "✅ Never trade with emotions – follow your plan!"
    )

def refer(update, context):
    user_id = update.message.from_user.id
    update.message.reply_text(
        f"🤝 Invite your friends and earn rewards!\n\n"
        f"Here is your personal referral link:\n"
        f"https://t.me/ForexCapital_Bot?start={user_id}"
    )

def contact(update, context):
    update.message.reply_text(
        "📩 Contact Support:\n\n"
        "If you need help, message us at @YourSupportUsername"
    )

# --- Message handler to map button presses ---
def handle_message(update, context):
    text = update.message.text
    if text == "📊 Signals":
        signals(update, context)
    elif text == "📈 Market":
        market(update, context)
    elif text == "📘 Strategy":
        strategy(update, context)
    elif text == "🤝 Refer":
        refer(update, context)
    elif text == "❓ Help":
        help_command(update, context)
    elif text == "📩 Contact":
        contact(update, context)
    else:
        update.message.reply_text("❌ Invalid option. Please use the menu buttons.")

# --- Main function ---

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("signals", signals))
    dp.add_handler(CommandHandler("market", market))
    dp.add_handler(CommandHandler("strategy", strategy))
    dp.add_handler(CommandHandler("refer", refer))
    dp.add_handler(CommandHandler("contact", contact))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start bot
    updater.start_polling()
    print("🤖 Bot is running with buttons...")
    updater.idle()

if __name__ == "__main__":
    main()
