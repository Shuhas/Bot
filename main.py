import ast

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from Evos_bot import *

try:
    create_table_log()
    create_table()
except Exception:
    pass


def btns(tip=None):
    btn = []
    if tip == 'til':
        btn = [
            [KeyboardButton("๐บ๐ฟ O'zbek tili")],
            [KeyboardButton("๐ท๐บ ะ ัััะบะธะน ัะทัะบ")],
            [KeyboardButton("๐บ๐ธ English language")]
        ]
    elif tip == 'menu':
        btn = [
            [KeyboardButton("๐ Gamburger"), KeyboardButton("๐ฏ Lavash")],
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
                InlineKeyboardButton(f"{i + 1}", callback_data=f"{i + 1}"),
                InlineKeyboardButton(f"{i + 2}", callback_data=f"{i + 2}")
            ])
        return InlineKeyboardMarkup(btn)
    else:
        btn = [
            [KeyboardButton("๐ฝ Katalog")],
            [KeyboardButton("๐ Buyurtmalarim"), KeyboardButton("๐ Savatcha")],
            [KeyboardButton("๐ Aksiya va yangiliklar"), KeyboardButton("โ๏ธBoglanish")]
        ]
    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def to_dict(strr):
    return ast.literal_eval(strr)


def start(update, context):
    user = update.message.from_user
    if get_user_log(user.id) and get_one(user.id):
        update.message.reply_text(f"Assalomu alaykum Ismingizni kiriting",
                                  reply_markup=btns('til'))
    else:
        create_user_log(user_id=user.id)
        create_user(user_id=user.id, username=user.username)
    log = to_dict(get_user_log(user.id)[0])
    log['state'] = 1
    change_log(message=log, user_id=user.id)


def message_handler(update, context):
    msg = update.message.text
    user = update.message.from_user
    log = to_dict(get_user_log(user.id)[0])
    if log.get('state', 0) == 1:
        log['ism'] = msg
        log['state'] = 2
        update.message.reply_text("Familiyangizni kiriting")
    elif log.get('state', 0) == 2:
        log['familiya'] = msg
        log['state'] = 3
        update.message.reply_text("Familiyangizni kiriting")

    change_log(user.id, log)


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
