from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import os

TOKEN = os.getenv("TOKEN")

def start(update: Update, context: CallbackContext):
    keyboard = [
        ['معرفی خدمات', 'رزرو نوبت'],
        ['نمونه کارها', 'تماس با ما'],
        ['آدرس', 'سوالات متداول']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('سلام! به ربات سالن زیبایی میترا میرزاده خوش آمدید. از منوی زیر یکی را انتخاب کنید.', reply_markup=reply_markup)

def services(update: Update, context: CallbackContext):
    update.message.reply_text('ما خدمات مختلفی مانند مراقبت از پوست، میکروبلیدینگ، آرایش و ... ارائه می‌دهیم.')

def reserve(update: Update, context: CallbackContext):
    update.message.reply_text('برای رزرو نوبت، لطفا تاریخ و ساعت مورد نظر را وارد کنید.')

def portfolio(update: Update, context: CallbackContext):
    update.message.reply_text('در اینجا نمونه کارهای سالن زیبایی میترا میرزاده را می‌بینید.')

def contact(update: Update, context: CallbackContext):
    update.message.reply_text('برای تماس با ما، لطفا با شماره ۰۹۱۲۳۴۵۶۷۸۹ تماس بگیرید.')

def address(update: Update, context: CallbackContext):
    update.message.reply_text('سالن زیبایی میترا میرزاده در خیابان انقلاب، پلاک ۱۰۴ واقع شده است.')

def faq(update: Update, context: CallbackContext):
    update.message.reply_text('1. چه خدماتی در سالن ارائه می‌دهید؟\n2. ساعات کاری سالن چیست؟')

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.regex('^معرفی خدمات$'), services))
    dispatcher.add_handler(MessageHandler(Filters.regex('^رزرو نوبت$'), reserve))
    dispatcher.add_handler(MessageHandler(Filters.regex('^نمونه کارها$'), portfolio))
    dispatcher.add_handler(MessageHandler(Filters.regex('^تماس با ما$'), contact))
    dispatcher.add_handler(MessageHandler(Filters.regex('^آدرس$'), address))
    dispatcher.add_handler(MessageHandler(Filters.regex('^سوالات متداول$'), faq))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
