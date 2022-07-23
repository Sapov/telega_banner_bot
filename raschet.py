import pyinputplus as pyip
price_banner = 350 # руб. за 1 метр кв.
price_luvers = 120 # рую. за 1 метр погонный
#     print("Введите номер для выбора".center(100,"="))
def razmer ():
    '''Запрашиваем размеры "Баннера" и спрашивае нужно ли поле для люверсов
    length_banner - Длина баннера
    whidh_banner - Ширина баннера'''

   # length_banner = float(input("Введите ширину баннера в метрах (например 1.2): ").replace(',', '.'))
   #  whidh_banner = input("Введите длину баннера в метрах: ").replace(',', '.')
    length_banner = pyip.inputFloat("Введите ширину печати в метрах: ")
    whidh_banner = pyip.inputFloat("Введите длину печати в метрах: ")

    pole_for_luvers = pyip.inputYesNo('''Нужно ли прибавить поля для установки люверсов или проклейки?
    Введите:
             Да.
             Нет. : ''', yesVal="да", noVal='нет')
    return length_banner, whidh_banner, pole_for_luvers




def dlina(l_banner,w_banner): # делаем длину больше ширины
    if w_banner > l_banner:
        l_banner, w_banner = w_banner, l_banner
    return l_banner, w_banner


# считаем площадь
def S_bannera(length_banner, whidh_banner):
    S = whidh_banner * length_banner
    print('Площадь равна', S, 'кв.м.')

def pole(whidh_banner, length_banner): #  прибавляем поля
    whidh_banner = whidh_banner + 0.1
    length_banner = length_banner + 0.1
    print('c полями баннер', whidh_banner,"м", 'x', length_banner,"м")
    return whidh_banner, length_banner


width_banner_list = [1.1, 1.37, 1.6, 2.2, 2.5, 3.2]
def select_banner(length_banner, whidh_banner, price_banner): # подбираем ширину ролика для печати
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
        # banner = []
        # banner.append(width_banner)
        # banner.append(length_banner)
        # print(banner)
        # считаем стоимсть печати умножаем ширину ролика на стоимтст прайса
        price_print = price_banner * width_banner * length_banner
        print("Стоимость печати баннера:", round(price_print, 1), "руб.")
        luvers = (width_banner + length_banner)*2*price_luvers
        print("Стоимость установки люверсов", round(luvers, 1), "руб.")
        print ("Стоимость баннера длинной", length_banner, "метра", "и шириной", width_banner, "метра с люверсами",round(luvers+price_print,1), "руб.")
    else:
        print("Нужна склейка")



def main(price_banner):
    length_banner, whidh_banner, pole_for_luvers = razmer()
    l, w = dlina(length_banner, whidh_banner) # меняем длину с шириной
    S_bannera(length_banner, whidh_banner)
    if pole_for_luvers == "да":
        l, w = pole(l, w)
    select_banner(l,w, price_banner)

# main(price_banner)

