# алгоритм расчета стоимости баннера
price_banner = 350 # руб. за 1 метр
price_luvers = 120 # руб. за 1 метр погонный
# length_banner = float(input("Введите ширину баннера в метрах (например 1.2): ").replace(',', '.'))
# whidh_banner = float(input("Введите длину баннера в метрах: ").replace(',', '.'))

def main(length_banner, whidh_banner):
# если длина меньше ширины мы меняем значения переменных местами ДЛИНА всегда у нас больше
    if length_banner < whidh_banner:
        length_banner, whidh_banner = whidh_banner, length_banner
           # прибавляем поля
    print("ШИРИНА", whidh_banner)
    print('Длина', length_banner)
    whidh_banner = whidh_banner + 0.1
    length_banner = length_banner + 0.1

    # # # # подбираем ширину ролика для печати
    #
    width_banner_list = (1.1, 1.37, 1.6, 2.2, 2.5, 3.2)
    if whidh_banner <= 3.1:
        for i in range(len(width_banner_list)):
            print("Подбираем ширину из списка", width_banner_list[i])
            if whidh_banner >= width_banner_list[i]:
                print("Нужен ролик шире", width_banner_list[i])
            else:
                print("Печатаем на ролике", width_banner_list[i])
                width_banner = width_banner_list[i]
                print("выбран ролик", width_banner, "метра")
                print("Печатаем длинной", length_banner, "метра")
                break

    elif whidh_banner >= 3.2:

        # тогда делим длинную сторону length_banner на 3.1
        price_print = "Не умею считать баннера со склейкаой. Пока!"
        print(price_print)


    # считаем стоимость печати умножаем ширину ролика на стоимость прайса и округляем
    price_print = round(price_banner * width_banner * length_banner, 1)

    print("Стоимость печати баннера:", price_print, "руб.")
    luvers = round((width_banner + length_banner) * 2 * price_luvers, 1)
    print("Стоимость установки люверсов", luvers, "руб.")
    print("Стоимость баннера длинной", width_banner, "метра", "и шириной", length_banner, "метра с люверсами",
          round(luvers + price_print, 1), "руб.")

    return price_print, luvers
