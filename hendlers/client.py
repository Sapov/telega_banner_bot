from aiogram import Dispatcher, types
import test
from create_bot import bot
from keybords import kb_client
from keybords import menu_banner
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text




# ******************************** КЛИЕНТСКАЯ ЧАСТЬ ****************************
# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, "Бот готов к работе. Посчитаю стоимость печати.", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему:\nhttps://t.me/bot_1")



class FSMAdmin(StatesGroup):
    width = State()
    length = State()
    pole = State()


async def banner_440 (message: types.Message):
    await FSMAdmin.width.set()
    await message.answer("Введите ширину в метрах ")

# !!!!!!
# @dp.message_handler(commands=["Печать на баннере"])
async def one_menu(message: types.Message):
    await message.reply("_", reply_markup=types.ReplyKeyboardRemove())# удаляем клавиатуру
    await bot.send_message(message.from_user.id, "Выберите плотность баннера: ", reply_markup=menu_banner)
    # await message.delete()

# @dp.message(Text("С CEТКА"))
async def print_setka(message: types.Message):
    await message.reply("СЕТКА --Отличный выбор!")

async def print_film(message: types.Message):
    await message.reply("Пленка --Отличный выбор!")

async def print_perfo(message: types.Message):
    await message.reply("Перфо --Отличный выбор!")

async def print_paper(message: types.Message):
    await message.reply("Бумага --Отличный выбор!")

async def print_oboi(message: types.Message):
    await message.reply("обои --Отличный выбор!")



# Ловим ответ
# @dp.message_handler(content_types=['width'],state = FSMAdmin.width)
async def load_width(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['whidh_banner'] = message.text
        await FSMAdmin.next()
        await message.reply("Введите длину в метрах")


# Ловим 2 ответ
# @dp.message_handler(state = FSMAdmin.length)
async def load_length(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        async with state.proxy() as data:
            data['length_banner'] = message.text
            # новая переменная меняем запятые на точки
            w = data['whidh_banner']
            l = data['length_banner']
            l = str(l.replace(',', '.'))
            w = str(w.replace(',', '.'))


            #ВЫлавлтваем не чмсленные значения
            try:
                l = float(l)
                w = float(w)
            except:
                print("Ошибка")
                await bot.send_message(message.from_user.id, f'Ошибка ввода {l} или {w}.')
                # ну и саязанные с ними не числами ошибки
            try:
                PRICE = test.main(l,w)
                await bot.send_message(message.from_user.id, f'Стоимость печати баннера длинной {l} метра, и шириной {w} метра составляет {PRICE[0]} руб. \n Установка люверсов стоит {PRICE[1]} руб. \n \n Итого: Стоимость баннера с люверсами {PRICE[0] + PRICE[1]} руб.')

            except:
                await state.finish()

# @bot.message_handler(content_types=['document'])
# async def handle_docs_photo(message):
#     ''' Сохранение файликов'''
#     await
#
#     try:
#         chat_id = message.chat.id
#
#         file_info = bot.get_file(message.document.file_id)
#         downloaded_file = bot.download_file(file_info.file_path)
#
#         src = 'C:/Users/sasha/PycharmProjects/telega_banner_bot/received/' + message.document.file_name;
#
#         with open(src, 'wb') as new_file:
#             new_file.write(downloaded_file)
#
#         bot.reply_to(message, "Пожалуй, я сохраню это")
#     except Exception as e:
#         bot.answer_inline_query(message, e)
#


# регистрируем хендлеры
def register_hendlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help', 'Назад'])
    dp.register_message_handler(one_menu, Text("Печать на баннере"), state=None)
    # dp.register_message_handler(print_setka, Text("Печать на сетке"))
    dp.register_message_handler(print_film, Text("Печать на пленке"))
    dp.register_message_handler(print_perfo, Text("Печать на перфопленке"))
    dp.register_message_handler(print_paper, Text("Печать на бумаге"))
    dp.register_message_handler(print_oboi, Text("Печать на фотообоях"))
    dp.register_message_handler(banner_440, Text("Баннер 440 грамм"), state=None)
    dp.register_message_handler(load_width, state=FSMAdmin.width)
    dp.register_message_handler(load_length, state=FSMAdmin.length)
    # @bot.message_handler(content_types=['document'])
    # dp.register_message_handler(handle_docs_photo, Text("Печать на сетке"))










