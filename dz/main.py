from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
import random


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

users_info = {}

def create_task():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    sign = random.choice(['+', '-'])
    return num1, sign, num2


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    id = message.from_user.id
    users_info[id] = create_task()
    await message.answer(text="Привет, этот бот улучшит твои навыки в арифметике!")
    await message.answer(text=f"Вот первый пример для тебя: {users_info[id][0]} {users_info[id][1]} {users_info[id][2]}")


@dp.message_handler()
async def send_example(message: types.Message):
    id = message.from_user.id

    if users_info[id][1] == '+':
        if message.text == str(users_info[id][0] + users_info[id][2]):
            await message.answer('Верно')
            users_info[id] = create_task()
            await message.answer(text=f"Новый пример для тебя: {users_info[id][0]} {users_info[id][1]} {users_info[id][2]}")
        else:
            await message.answer('Неверно, попробуй еще раз')

    elif users_info[id][1] == '-':
        if message.text == str(users_info[id][0] - users_info[id][2]):
            await message.answer('Верно')
            users_info[id] = create_task()
            await message.answer(text=f"Новый пример для тебя: {users_info[id][0]} {users_info[id][1]} {users_info[id][2]}")
        else:
            await message.answer('Неверно, попробуй еще раз')


if __name__ == '__main__':
    executor.start_polling(dp)
