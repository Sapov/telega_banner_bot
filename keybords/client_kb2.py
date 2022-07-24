from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
b1 = KeyboardButton('/Меню')
b2 = KeyboardButton ('/Печать на баннере 330грамм')
b3 = KeyboardButton ('/440_грамм')
# b4 =KeyboardButton ( "Поделится номером ", request_contact=True)
# b5 = KeyboardButton ( "место локации ", request_location=True)

# Замещаем обычную клавиатуру нашей
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1,b2).add(b3)#.add(b4).add(b5)
# Написать меню для бота: вход для клиентов и для РА
### расчет стоимости баннера и пленки и бумаги