"""
Professional Telegram Customer Service Bot
Handles common customer inquiries with automated responses
"""

import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Conversation states
MENU, CONTACT, TRACKING = range(3)


class CustomerServiceBot:
    """Main bot class handling all interactions"""

    def __init__(self, token: str):
        """Initialize bot with token"""
        self.token = token
        self.application = Application.builder().token(token).build()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send welcome message when /start is issued"""
        user = update.effective_user
        welcome_message = f"""
👋 Welcome {user.first_name}!

I'm your automated customer service assistant. I can help you with:

🔹 Product Information
🔹 Order Tracking
🔹 FAQs
🔹 Contact Support
🔹 Business Hours

Type /menu to see all available options!
        """
        await update.message.reply_text(welcome_message)

    async def menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Display main menu with options"""
        keyboard = [
            ['📦 Track Order', '💬 Contact Us'],
            ['❓ FAQs', '🕐 Business Hours'],
            ['💡 Products', '🏪 About Us']
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

        await update.message.reply_text(
            '📋 Main Menu\n\nPlease select an option:',
            reply_markup=reply_markup
        )

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle text messages based on user selection"""
        text = update.message.text.lower()

        if 'track order' in text or '📦' in text:
            response = """
📦 Order Tracking

To track your order, please provide:
• Order number (e.g., ORD-12345)
• Email address used for purchase

You can also track orders at: www.example.com/track

Need help? Type /contact
            """

        elif 'contact' in text or '💬' in text:
            response = """
💬 Contact Support

📧 Email: support@example.com
📞 Phone: +1 (555) 123-4567
💬 Live Chat: Available on our website

Business Hours: Mon-Fri, 9 AM - 6 PM EST

We typically respond within 24 hours!
            """

        elif 'faq' in text or '❓' in text:
            response = """
❓ Frequently Asked Questions

Q: What is your return policy?
A: 30-day money-back guarantee on all products.

Q: Do you ship internationally?
A: Yes! We ship to over 100 countries.

Q: How long does shipping take?
A: 3-5 business days domestic, 7-14 days international.

Q: Do you offer discounts?
A: Subscribe to our newsletter for exclusive deals!

More questions? Type /contact
            """

        elif 'business hours' in text or '🕐' in text:
            response = """
🕐 Business Hours

Monday - Friday: 9:00 AM - 6:00 PM EST
Saturday: 10:00 AM - 4:00 PM EST
Sunday: Closed

Holidays: Closed on major US holidays

Outside business hours? Leave us a message at support@example.com
            """

        elif 'products' in text or '💡' in text:
            response = """
💡 Our Products

🔹 Category 1: Premium Solutions
🔹 Category 2: Standard Plans
🔹 Category 3: Custom Services

Visit our catalog: www.example.com/products

Need recommendations? Type /contact to speak with our team!
            """

        elif 'about' in text or '🏪' in text:
            response = """
🏪 About Us

We're a leading provider of [your service/product].

✨ Founded: 2020
🌍 Serving: 50+ countries
👥 Team: 100+ professionals
⭐ Rating: 4.9/5 (5000+ reviews)

Our mission: Deliver exceptional quality and service to every customer.

Learn more: www.example.com/about
            """

        else:
            response = """
I'm not sure I understand.

Type /menu to see available options, or /help for assistance.
            """

        await update.message.reply_text(response)

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send help message"""
        help_text = """
🤖 Bot Commands

/start - Welcome message
/menu - Show main menu
/help - Show this help message
/contact - Contact information
/track - Track your order
/cancel - Close keyboard

Just click any menu button or type your question!
        """
        await update.message.reply_text(help_text)

    async def contact_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send contact information"""
        contact_text = """
📞 Contact Information

📧 Email: support@example.com
📞 Phone: +1 (555) 123-4567
💬 Website: www.example.com
🏢 Address: 123 Business St, City, State 12345

Business Hours:
Monday-Friday: 9 AM - 6 PM EST

We're here to help! 😊
        """
        await update.message.reply_text(contact_text)

    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Cancel and remove keyboard"""
        await update.message.reply_text(
            'Menu closed. Type /menu to open again!',
            reply_markup=ReplyKeyboardRemove()
        )

    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Log errors"""
        logger.error(f'Update {update} caused error {context.error}')

    def run(self):
        """Start the bot"""
        # Register handlers
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("menu", self.menu))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("contact", self.contact_command))
        self.application.add_handler(CommandHandler("cancel", self.cancel))

        # Handle text messages
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message)
        )

        # Error handler
        self.application.add_error_handler(self.error_handler)

        # Start bot
        logger.info("Bot started successfully!")
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)


# Main execution
if __name__ == '__main__':
    print("="*60)
    print("TELEGRAM CUSTOMER SERVICE BOT")
    print("="*60)
    print("\nTo run this bot, you need:")
    print("1. A Telegram Bot Token from @BotFather")
    print("2. Python library: python-telegram-bot")
    print("\nInstall with: pip install python-telegram-bot")
    print("="*60)

    # Replace with your actual bot token
    BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("\n⚠️  Please set your bot token!")
        print("\nHow to get a token:")
        print("1. Open Telegram and search for @BotFather")
        print("2. Send /newbot and follow instructions")
        print("3. Copy the token and paste it in this script")
        print("4. Run the script again!")
    else:
        # Create and run bot
        bot = CustomerServiceBot(BOT_TOKEN)
        bot.run()
