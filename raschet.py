""" универсальный модуль расчета стоимости печати на материале
1/ передается название материала
1.1 узнаем цену материала
1.2. устанавливаем ширины материала
1.3. считаем"""
price_luvers = 120
from data import *


def price(material_name):
    print("SEND", material_name)

    return material_banner[material_name]

def dlina(l_banner, w_banner):  # делаем длину больше ширины
    if w_banner > l_banner:
        l_banner, w_banner = w_banner, l_banner
    return l_banner, w_banner


def pole(whidh_banner, length_banner):  # прибавляем поля
    whidh_banner = whidh_banner + 0.1
    length_banner = length_banner + 0.1
    print('c полями баннер', whidh_banner, "м", 'x', length_banner, "м")
    return whidh_banner, length_banner


def materials(material_name):
    '''функция получает на вход название материала и определяет ширины роликов материалов'''
# if material_name == "Баннер 440 грамм":
#     print("Выбираем ролики - размеры 440 банера")

width_banner_list = [1.1, 1.37, 1.6, 2.2, 2.5, 3.2]
whidth_film_oraget_list = [1.05, 1.26, 1.37, 1.52]
whidth_film_china_list = [1.07, 1.27, 1.37, 1.5]
whidth_paper = [1.26, 1.3, 1.6]
whidth_setka = [3.2]


def select_banner(length_banner, whidh_banner, price_banner):  # подбираем ширину ролика для печати
    # global width_banner
    if whidh_banner < 3.1:
        for i in range(len(width_banner_list)):
            # print("Подбираем ширину из списка", width_banner_list[i])
            if whidh_banner >= width_banner_list[i]:
                pass
                # print("Нужен ролик шире", width_banner_list[i])

            else:
                print("Печатаем на ролике", width_banner_list[i])
                width_banner: float = width_banner_list[i]
                break
        print("выбран ролик ШИРИНОЙ", width_banner, "метра")
        print("Печатаем длинной", length_banner, "метра")

        # считаем стоимость печати умножаем ширину ролика на стоимтсть прайса
        price_print = price_banner * width_banner * length_banner
        print("Стоимость печати баннера:", round(price_print, 1), "руб.")
        luvers = (width_banner + length_banner) * 2 * price_luvers
        print("Стоимость установки люверсов", round(luvers, 1), "руб.")
        print("Стоимость баннера длинной", length_banner, "метра", "и шириной", width_banner, "метра с люверсами",
              round(luvers + price_print, 1), "руб.")
    else:
        print("Нужна склейка")


def main(length_banner, whidh_banner, pole_for_luvers, material_name):
    l, w = dlina(length_banner, whidh_banner)  # меняем длину с шириной
    if pole_for_luvers == "да":
        l, w = pole(l, w)
    price_banner = price(material_name)
    select_banner(l, w, price_banner)

# main(price_banner)
