from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
                          InlineKeyboardMarkup, InlineKeyboardButton

from main import bot, client


async def race_choice(user, locale):
    mrc = InlineKeyboardMarkup(row_width=2,
            inline_keyboard = [
                [
                    InlineKeyboardButton(
                        text = locale['race:people'],
                        callback_data = 'mrc:people'
                        ),
                    InlineKeyboardButton(
                        text = locale['race:elves'],
                        callback_data = 'mrc:elves'
                        )
                ],
                [
                    InlineKeyboardButton(
                        text = locale['race:gnomes'],
                        callback_data = 'mrc:gnomes'
                        ),
                    InlineKeyboardButton(
                        text = locale['race:orcs'],
                        callback_data = 'mrc:orcs'
                        )
                ]
            ]
    )

    await bot.send_message(
            user,
            locale['race:choice'],
            reply_markup = mrc
            )
