import asyncio
from aiogram import Bot, Dispatcher, F, Command
from dotenv import dotenv_values
from backend import get_random_agressive_line, generate_random_ip
from users.users import create_user

from keyboards import test_keyboard



config = dotenv_values()

bot = Bot(token=config["BOT_TOKEN"])

dp = Dispatcher()

@dp.message(Command('start'))
async def start_cmd(message):
    user_id = message.from_user.id
    config = {
        "ip": generate_random_ip(),
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "username": message.from_user.username,
        "language_code": message.from_user.language_code
    }
    create_user(user_id = user_id, config = config)
    first_name = config['first_name']
    await message.reply("Тест", reply_markup=test_keyboard())


@dp.callback_query(F.data == 'test')
async def answer_query(callback):
    await callback.message.reply('Успещный тест')


@dp.message(F.text)
async def text_message(message):
    await message.reply(get_random_agressive_line)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
