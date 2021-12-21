from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from Evos_bot import *

try:
    create_table()
except Exception as e:
    pass


def btns(tip=None):
    btn = []
    if tip == 'til':
        btn = [
            [KeyboardButton("🇺🇿 O'zbek tili")],
            [KeyboardButton("🇷🇺 Русский язык")],
            [KeyboardButton("🇺🇸 English language")]
        ]
    elif tip == 'menu':
        btn = [
            [KeyboardButton("🍔 Gamburger"), KeyboardButton("🌯 Lavash")],
        ]
    elif tip == 'gamburger':
        btn = [
            [KeyboardButton("BBQ Burger"), KeyboardButton("BBQ Cheese Burger")],
            [KeyboardButton("Cheese burger"), KeyboardButton("Chicken burger")],
            [KeyboardButton("Chicken Cheese burger"), KeyboardButton("Double Cheese burger")]
        ]
    elif tip == "numbers":
        btn = []
        for i in range(1, 9, 3):
            btn.append([
                InlineKeyboardButton(f"{i}", callback_data=f"{i}"),
                InlineKeyboardButton(f"{i+1}", callback_data=f"{i+1}"),
                InlineKeyboardButton(f"{i+2}", callback_data=f"{i+2}")
            ])
        return InlineKeyboardMarkup(btn)
    else:
        btn = [
            [KeyboardButton("🍽 Katalog")],
            [KeyboardButton("🛍 Buyurtmalarim"), KeyboardButton("🛒 Savatcha")],
            [KeyboardButton("🎉 Aksiya va yangiliklar"), KeyboardButton("☎️Boglanish")]
        ]
    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def start(update, context):
    user = update.message.from_user
    print(user)
    update.message.reply_text(f"Assalomu alaykum {user.first_name}\nTilni tanlang 👇",
                              reply_markup=btns('til'))


def message_handler(update, context):
    msg = update.message.text
    if msg == "🇺🇿 O'zbek tili":
        update.message.reply_text("Bu yerda siz menyu bilan tanishishingiz va uyga buyurtma berishingiz mumkin!\n"
                                  "\nMahsulotlarni 🍽 Katalog bo‘limidan tanlang", reply_markup=btns())
    elif msg == "🍽 Katalog":
        update.message.reply_html("Kategoriyalardan birini tanlang 👇", reply_markup=btns('menu'))
    elif msg == "🍔 Gamburger":
        update.message.reply_text("Tanishib chiqish uchun kategoriyani tanlang 👇",
                                  reply_markup=btns('gamburger'))
    elif msg == "BBQ Burger":
        context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open("Gamburger.jpg", "rb"),
            caption="BBQ Burger\nNarxi: 23 000 so'm\n\nSonini tanlang yoki kiriting:",
            reply_markup=btns("numbers")
        )
    elif msg.isdigit():
        update.message.reply_text(f"{int(msg) * 23000} so'm")


def inline_handler(update, context):
    query = update.callback_query
    data = query.data
    query.message.reply_text(f"{int(data) * 23000} so'm")


def main():
    TOKEN = "2143262194:AAE21Y2r7pp4o-5RqJXII7fLlgqOXopYg5s"
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
