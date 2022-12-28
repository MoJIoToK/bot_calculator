from telebot import TeleBot, types
import os

TOKEN = ''

bot = TeleBot(TOKEN)


dct = {}


@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    dct[msg.from_user.id] = []
    bot.send_message(chat_id=msg.from_user.id, text=f'Здравствуйте! Вас приветствует бот калькулятор.'
                        '\nДанный бот выполняет простейшие арифметические действия, в том числе с комплексными числами.'
                        '\nКомплексные числа записываются через j после коэффициента. Пример a+bj'
                        '\nВведите арифметическую операцию')


@bot.message_handler(commands=['log'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Вывожу лог')


@bot.message_handler()
def answer(msg: types.Message):
    text = msg.text
    if text == '+':
        bot.register_next_step_handler(msg, sum_)
        bot.send_message(chat_id=msg.from_user.id, text='Введите слагаемые')
    elif text == '-':
        bot.register_next_step_handler(msg, sub_)
        bot.send_message(chat_id=msg.from_user.id, text='Введите уменьшаемое и вычитаемое')
    elif text == '*':
        bot.register_next_step_handler(msg, mult_)
        bot.send_message(chat_id=msg.from_user.id, text='Введите умножаемое и множитель')
    elif text == '/':
        bot.register_next_step_handler(msg, div_)
        bot.send_message(chat_id=msg.from_user.id, text='Введите делимое и делитель')
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text +
                                                        ', а должны были арифметическое действие')

def is_complex(ex):
    flag = True if "j" in ex else False
    if flag:
        return complex(ex)
    return float(ex)


def sum_(msg):
    a, b = map(is_complex, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Вы ввели число неправильного формата. Для продолжения введите /start') 
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')
    bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')


def sub_(msg):
    a, b = map(is_complex, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {a - b}')
    bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')


def mult_(msg):
    a, b = map(is_complex, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат умножения {a * b}')
    bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')


def div_(msg):
    a, b = map(is_complex, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат деления {a / b}')
    bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')


bot.polling()