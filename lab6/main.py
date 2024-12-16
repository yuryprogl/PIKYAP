from aiogram import types, executor, Dispatcher, Bot
from aiogram.dispatcher.filters import Text

from config import TOKEN_API
from keyboard import kb, kb_photo
import random

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
/start - запуск бота
/help - команды бота
/description - описание бота
"""

photos = [
    "https://a.d-cd.net/sAAAAgFICuA-960.jpg",
    "https://twizz.ru/wp-content/uploads/2018/07/2rqlo3qgiv9vggpwibspndkfh4v50mngqzt2ghnlfo.jpg",
    "https://i.imgur.com/OvflPTZ.jpg"
]

async def on_startup(_):
    print('Я был запущен')


@dp.message_handler(Text(equals='Random photo'))
async def send_kb_photo(message: types.Message):
    await message.answer('Чтобы отправить рандомную фотографию нажми на кнопку "Рандом"',
                         reply_markup=kb_photo)


@dp.message_handler(Text(equals='Главное меню'))
async def open_kb(message: types.Message):
    await message.answer('Добро пожаловать в главное меню',
                         reply_markup=kb)

@dp.message_handler(Text(equals='Рандом'))
async def send_photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random.choice(photos))


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Привет, дорогой друг!',
                         reply_markup=kb)



@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(HELP_COMMAND)


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer('Наш бот умеет много чего')
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgIAAxkBAAEIq_hkQqSNRRrn1VF5XCXmi-uh4Y8PswACDBMAAoiEyEsOauMaYVUKKy8E')
    print(message.chat.id)

if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)
