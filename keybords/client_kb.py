from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
b1 = KeyboardButton('Печать на баннере')
b2 = KeyboardButton('Печать на сетке')
b3 = KeyboardButton('Печать на пленке')
b4 = KeyboardButton('Печать на перфопленке')
b5 = KeyboardButton('Печать на бумаге')
b6 = KeyboardButton('Печать на фотообоях')

ba1 = KeyboardButton('Баннер 440 грамм')
ba2 = KeyboardButton('Баннер 330 грамм')
ba3 = KeyboardButton('Баннер 510 грамм')


# Замещаем обычную клавиатуру нашей
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1, b2).add(b3).add(b4).add(b5).add(b6)
# Написать меню для бота: вход для клиентов и для РА
### расчет стоимости баннера и пленки и бумаги

kb_client_banner = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_banner.add(ba1).add(ba2).add(ba3)
# Написать меню для бота: вход для клиентов и для РА
### расчет стоимости баннера и пленки и бумаги