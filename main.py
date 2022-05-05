from aiogram import Bot, Dispatcher, executor, md, types
import os, sys, random
import comp
import res.lang


with open('config/api_token') as file_api_token:
    file_content = file_api_token.read()
    exec('%s = %s' % tuple(file_content.split(' ', 1)))


bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
client = Dispatcher(bot)

@client.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = comp.MGMT(message.from_user.id).get_user()

    if user == None:
        comp.MGMT(message.from_user.id).add_user(message.from_user)
        await message.reply('Начало игры')

    else:
        #locale = res.lang.ru if message.from_user.locale == 'ru' else res.lang.en
        locale = res.lang.ru
        #await comp.main_menu()



if __name__ == '__main__':
    executor.start_polling(client, skip_updates=True)
