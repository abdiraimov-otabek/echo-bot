import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

TOKEN = getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@router.message(Command(commands=["help"]))
async def command_help_handler(message: Message) -> None:
    await message.answer("This is a simple echo bot. It will reply with the same message you sent.")
    
@router.message(Command(commands=['say_hello']))
async def command_say_hello_handler(message: Message) -> None:
    await message.answer("Hello!")

@router.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")

dp.include_router(router)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.run_polling(bot)