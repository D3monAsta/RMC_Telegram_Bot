import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram
from aiogram.utils.exceptions import BotBlocked
import aiogram.utils.markdown as fmt
from aiogram.types import InputFile, chat, contact, reply_keyboard
from random import choice
import keyboards as kb
from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted, MessageToDeleteNotFound)
import emoji
from os import path, listdir

bot = Bot(token="6298134701:AAGtJ4IL03IueqClTvfZjquiKkqXTb7mYbA")

startText = """Добрый день!

Команда РМЦ ответит на все интересующие Вас вопросы по получению социального сертификата дополнительного образования детей в Ростовской области.
"""
infoText = """А вы подписаны на наши социальные сети?
Будьте в курсе событий!""" + emoji.emojize(":slightly_smiling_face:")+"""Присоединяйтесь к РМЦ!"""+emoji.emojize(":glowing_star:")

#Inline keyboard
inline_btn_1 = types.InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb1 = types.InlineKeyboardMarkup().add(inline_btn_1)

# Bot body
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

async def set_default_comands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("ask", "Задать вопрос"),
        types.BotCommand("share", "Поделиться информацией")
    ])

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer(startText, reply_markup=kb.inf_kb)
    await message.answer(infoText, reply_markup=kb.rmc_kb)
    await message.answer('Если вы не нашли ответа на свой вопрос, пожалуйста, уточните, что вас интересует, и мы поможем вам получить нужную информацию.',reply_markup=kb.main_kb)

@dp.message_handler(lambda message: message.text == "Задать вопрос")
async def AskQuestion(message: types.Message):
    await message.answer("Напишите нам свой вопрос здесь"+emoji.emojize(":down_arrow:"), reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(lambda message: message.text == "Поделиться информацией")
async def ShareInfo(message: types.Message):
    await message.answer("Хотите поделиться информацией о дополнительном образовании детей региона?", reply_markup=kb.ask_kb)

@dp.message_handler(lambda message: message.text == "Да")
async def yes(message: types.Message):
    await message.answer("Напиите свою информацию здесь"+emoji.emojize(":down_arrow:"), reply_markup=types.ReplyKeyboardRemove())

@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print(f"User blocked me!\nMessage: {update}\nError: {exception}")
    return True

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)