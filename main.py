from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ['معرفی خدمات', 'رزرو نوبت'],
        ['نمونه کارها', 'تماس با ما'],
        ['آدرس', 'سوالات متداول']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        'سلام! به ربات سالن زیبایی میترا میرزاده خوش آمدید. از منوی زیر یکی را انتخاب کنید.',
        reply_markup=reply_markup
    )

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('ما خدمات مختلفی مانند مراقبت از پوست، میکروبلیدینگ، آرایش و ... ارائه می‌دهیم.')

async def reserve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('برای رزرو نوبت، لطفا تاریخ و ساعت مورد نظر را وارد کنید.')

async def portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('در اینجا نمونه کارهای سالن زیبایی میترا میرزاده را می‌بینید.')

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('برای تماس با ما، لطفا با شماره ۰۹۱۲۳۴۵۶۷۸۹ تماس بگیرید.')

async def address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('سالن زیبایی میترا میرزاده در خیابان انقلاب، پلاک ۱۰۴ واقع شده است.')

async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('1. چه خدماتی در سالن ارائه می‌دهید؟\n2. ساعات کاری سالن چیست؟')

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex("^معرفی خدمات$"), services))
    app.add_handler(MessageHandler(filters.Regex("^رزرو نوبت$"), reserve))
    app.add_handler(MessageHandler(filters.Regex("^نمونه کارها$"), portfolio))
    app.add_handler(MessageHandler(filters.Regex("^تماس با ما$"), contact))
    app.add_handler(MessageHandler(filters.Regex("^آدرس$"), address))
    app.add_handler(MessageHandler(filters.Regex("^سوالات متداول$"), faq))

    app.run_polling()

if __name__ == '__main__':
    main()
