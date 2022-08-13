from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
ba1 = KeyboardButton('Баннер 440 грамм')
ba2 = KeyboardButton('Баннер 330 грамм')
ba3 = KeyboardButton('Баннер_510_грамм')
ba4 = KeyboardButton('/Назад')


# Замещаем обычную клавиатуру нашей
menu_banner = ReplyKeyboardMarkup(resize_keyboard=True)
menu_banner.add(ba1).add(ba2).add(ba3).add(ba4)
# Написать меню для бота: вход для клиентов и для РА
### расчет стоимости баннера и пленки и бумаги