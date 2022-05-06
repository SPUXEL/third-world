from aiogram import Bot, Dispatcher, executor, md, types
import os, sys, random
import comp, lang


with open('config/api_token') as file_api_token:
    file_content = file_api_token.read()
    exec('%s = %s' % tuple(file_content.split(' ', 1)))

bot = Bot(token=API_TOKEN)
#bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
client = Dispatcher(bot)

# --- START ---
@client.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = comp.MGMT(message.from_user.id).get_user()

    locale = lang.ru
    #locale = lang.ru if message.from_user.locale == 'ru' else lang.en

    if user == None:
        #comp.MGMT(message.from_user.id).add_user(message.from_user)
        await comp.race_choice(message.from_user.id, locale)

    else:
        #await comp.main_menu()
        pass

# --- RACE CHOICE ---
@client.callback_query_handler(text=['mrc:people', 'mrc:elves', 'mrc:gnomes', 'mrc:orcs'])
async def send_message(call: types.CallbackQuery):

    locale = lang.ru
    #locale = lang.ru if message.from_user.locale == 'ru' else lang.en

    if call.data == 'mrc:people':
        await call.message.answer('People')
        await call.answer(text = locale['race:people:chosen'])

    elif call.data == 'mrc:elves':
        await call.message.answer('Elves')
        await call.answer(text = locale['race:elves:chosen'])

    elif call.data == 'mrc:gnomes':
        await call.message.answer('Gnomes')
        await call.answer(text = locale['race:gnomes:chosen'])

    elif call.data == 'mrc:orcs':
        await call.message.answer('Orcs')
        await call.answer(text = locale['race:orcs:chosen'])


if __name__ == '__main__':
    executor.start_polling(client, skip_updates=True)
