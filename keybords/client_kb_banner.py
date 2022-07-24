from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
ba1 = KeyboardButton('/Баннер 440 грамм')
ba2 = KeyboardButton ('/Баннер 330 грамм')
ba3 = KeyboardButton ('/Баннер 510 грамм')


# Замещаем обычную клавиатуру нашей
kb_client_banner = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_banner.add(ba1).add(ba2).add(ba3)
# Написать меню для бота: вход для клиентов и для РА
### расчет стоимости баннера и пленки и бумаги