from imaplib import Commands
from click import command
import telebot

from telebot import types

# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

bot = telebot.TeleBot('5475773276:AAE-YwDBBeSxUCl4DTLFt6x-bcEHC9hMGsM')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('О нас', url='https://enactus.kg/about-us/'))
    bot.send_message(message.chat.id, f'''Здравствуйте, {message.from_user.first_name} {message.from_user.last_name},
Вас приветсвует команда Enactus KSTU
Enactus, ранее известная как SIFE — крупнейшая международная некоммерческая организация,
которая объединяет студентов, лидеров бизнеса и университеты,
идеей использования силы предпринимательства для изменения жизни людей и
формирования лучшего, более устойчивого мира.''', reply_markup=markup)

@bot.message_handler(commands=['departments'])
def departments(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    fin = types.KeyboardButton('/Finance')
    funrise = types.KeyboardButton('/FunRise')
    it_dep = types.KeyboardButton('/IT')
    pr_dep = types.KeyboardButton('/PR')
    hr_dep = types.KeyboardButton('/HR')
    proj_dep = types.KeyboardButton('/ProjectDep')
    markup.add(fin, funrise, it_dep, pr_dep, hr_dep, proj_dep)
    bot.send_message(message.chat.id, 'Выберите отдел', reply_markup=markup)

# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, 'Отличное фото', parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Finance':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Задание', url='https://enactus.kg/about-us/'))
        bot.send_message(message.chat.id, f'''Здравствуйте, {message.from_user.first_name} {message.from_user.last_name},
Пока что бот находится в стадии разработки и тестовых проверок.
Задания для финансового отдела пока нет''', reply_markup=markup)
    elif message.text == 'FunRise':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Задание', url='https://enactus.kg/about-us/'))
        bot.send_message(message.chat.id, f'''Здравствуйте, {message.from_user.first_name} {message.from_user.last_name},
Пока что бот находится в стадии разработки и тестовых проверок.
Задания для фанрайз отдела пока нет''', reply_markup=markup)
    elif message.text == 'IT':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Задание', url='https://enactus.kg/about-us/'))
        bot.send_message(message.chat.id, f'''Здравствуйте, {message.from_user.first_name} {message.from_user.last_name},
Пока что бот находится в стадии разработки и тестовых проверок.
Задания для IT отдела пока нет''', reply_markup=markup)
    elif message.text == 'PR':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Задание', url='https://enactus.kg/about-us/'))
        bot.send_message(message.chat.id, f'''Здравствуйте, {message.from_user.first_name} {message.from_user.last_name},
Пока что бот находится в стадии разработки и тестовых проверок.
Задания для PR отдела пока нет''', reply_markup=markup)
    elif message.text == 'HR':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Задание', url='https://enactus.kg/about-us/'))
        bot.send_message(message.chat.id, f'''Здравствуйте, {message.from_user.first_name} {message.from_user.last_name},
Пока что бот находится в стадии разработки и тестовых проверок.
Задания для HR отдела пока нет''', reply_markup=markup)
    elif message.text == 'ProjectDep':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Задание', url='https://enactus.kg/about-us/'))
        bot.send_message(message.chat.id, f'''Здравствуйте, {message.from_user.first_name} {message.from_user.last_name},
Пока что бот находится в стадии разработки и тестовых проверок.
Задания для Проектно-исследовательского отдела пока нет''', reply_markup=markup)


@bot.message_handler(commands=['/Finance'])
def get_user_text(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Задание для Фин отдела', url='https://enactus.kg/about-us/'))
    bot.send_message(message.chat.id, f'''Здравствуйте, {message.from_user.first_name} {message.from_user.last_name},
Пока что бот находится в стадии разработки и тестовых проверок.
Задания для финансового отдела пока нет''', reply_markup=markup)
 
bot.polling(none_stop=True)