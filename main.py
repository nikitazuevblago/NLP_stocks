import datetime

from aiogram import Bot, types
from aiogram import Dispatcher
import logging
import asyncio
from aiogram.filters.command import Command, CommandObject
import sqlite3
from LLM_result import NLP_stocks
from secret_key import bot_token


bot = Bot(token=bot_token)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

email_validate_pattern = r"^\S+@\S+\.\S+$"

price = 150


@dp.message(Command(commands=["start", "set_balance", "profile", "change_email", "request"]))
async def start_message(msg: types.Message, command: CommandObject):
    if command.command == "start":
        ids = cursor.execute('''
    select user_id from Users
        ''')
        if msg.from_user.id not in ids:
            cursor.execute(f'''
    INSERT INTO Users (username, user_id, email, balance, is_request) 
    VALUES ("{msg.from_user.username}", "{msg.from_user.id}", "Not Set", "0", "FALSE")
                ''')
            connection.commit()
        await bot.send_message(msg.from_user.id, "Select the desired menu section:")

    if command.command == "set_balance":
        arg = command.args
        if not arg is None:
            if arg.isnumeric() and arg != 0:
                cursor.execute(f'''
                UPDATE Users SET balance = {arg} WHERE user_id = {msg.from_user.id};
                ''')
                connection.commit()
            await bot.send_message(msg.from_user.id, f"successfully added {arg} to balance")
        else:
            await bot.send_message(msg.from_user.id, "Invalid data format")

    if command.command == "profile":
        balance = cursor.execute(f'''
                        SELECT balance FROM Users WHERE user_id = {msg.from_user.id}
                            ''').fetchone()[0]
        await bot.send_message(msg.from_user.id,
                               f"{msg.from_user.username}'s Profile:\nBalance: {balance}\n\n To set balance, write /set_balance "
                               f"COUNT")

    if command.command == "request":
        arg = command.args
        if not(arg is None):
            arg = arg.upper()
            balance = cursor.execute(f'''
                    SELECT balance FROM Users WHERE user_id = {msg.from_user.id}
                        ''').fetchone()[0]
            if int(balance) >= price:
                user_id = msg.from_user.id
                username = cursor.execute(f'''
                        SELECT username FROM Users WHERE user_id = {user_id}
                            ''').fetchone()[0]
                await bot.send_message(-1001652909098,
                                       f"Time: {datetime.datetime.now().time()}\nUser_id: {user_id}\nUsername: @{username}\nTicker: {arg}")
                bal = balance - price
                cursor.execute(f'''
                                    UPDATE Users SET balance = {bal} WHERE user_id = {msg.from_user.id};
                                    ''')
                connection.commit()
                await bot.send_message(msg.from_user.id, "Wait for answer")
                answer = NLP_stocks(arg)
                if len(answer) > 4096:
                    for x in range(0, len(answer), 4096):
                        await bot.send_message(msg.from_user.id, answer[x:x + 4096])
                else:
                    await bot.send_message(msg.from_user.id, answer)
            else:
                await bot.send_message(msg.from_user.id,
                                       "There is not enough money on the balance, pay it up")
        else:
            await bot.send_message(msg.from_user.id, "Invalid ticker")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
