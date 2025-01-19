import asyncio
from aiogram import Bot, Dispatcher, F
from dotenv import dotenv_values
from backend import get_random_agressive_line, generate_random_ip

config = dotenv_values()


bot = Bot(token=config["TOKEN"])

dp = Dispatcher()

@dp.message(F.text)
async def text_message(message):
    await message.reply(get_random_agressive_line)




async def main():
    await dp.start_polling(bot)


asyncio.run(main())
