from aiogram import Dispatcher, types
import test
from create_bot import bot
from keybords import kb_client
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


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


# начала диалога
# @dp.message_handler(commands = "Загрузить", state = None)
async def cn_start(message: types.Message):
    await FSMAdmin.width.set()
    await message.answer("Введите ширину баннера в метрах ")


# Ловим ответ
# @dp.message_handler(content_types=['width'],state = FSMAdmin.width)
async def load_width(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['whidh_banner'] = message.text
        await FSMAdmin.next()
        await message.reply("Введите длину баннера в метрах")


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
            print(type(l))

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


# регистрируем хендлеры
def register_hendlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])

    dp.register_message_handler(cn_start, commands="440_грамм", state=None)
    dp.register_message_handler(load_width, state=FSMAdmin.width)
    dp.register_message_handler(load_length, state=FSMAdmin.length)




