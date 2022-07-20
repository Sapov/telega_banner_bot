# from data import *

price_banner = 350 # руб. за 1 метр кв.
price_luvers = 120 # рую. за 1 метр погонный

#
# # ----- функция перебираеем словарь и выводим в менюшку
#
# def print_menu(dic_material):
#     print("Введите номер для выбора типа материала:".center(100, "-"))
#     index_b = 0
#     materials = []
#     for k in dic_material.keys():
#         index_b += 1
#         print(f'{index_b}.{k}')
#         materials.append(k)
#
#     print("Введите номер для выбора".center(100,"="))
#     while True:
#         numer_material = input("Введите цифру: ")
#         ### проверяем если numer_material равен цифре -1 и не больше чем len(materials)
#         if numer_material == "1" and float(numer_material) <= len(materials):
#             print("Считаем", materials[0])
#             break
#         elif numer_material == "2" and float(numer_material) <= len(materials):
#             print("Считаем", materials[2-1])
#             break
#         elif numer_material == "3" and float(numer_material) <= len(materials):
#             print("Считаем", materials[2])
#             break
#         else:
#             print("Введите правильную цифру")
#
# #____________________________________________________
#
# print(" Выбираем материал для широкоформатной печати: ".center(100,"*") + "\n" "Введите номер для выбора типа материала:")
# index_1 = 0
# for item in range(len(fist_change_material)):
#     index_1 +=1
#     print(f'{index_1}. {fist_change_material[item]}')
#
# while True:
#     number_material = input("Введите номер: ")
#     if number_material == "4":
#         for k in price_material.keys():
#             print(k)
#
#             break
#     elif number_material == "1":
#         # print('\n')
#         # ----- функция перебираеем словарь  и вывдим в менюшку
#         print_menu(banner)
#
#         break
#
#
#     elif number_material == "2":
#         print("Fim")
#         print_menu(film)
#
#         break
#     elif number_material == "3":
#         print("Paper")
#         print_menu(paper)
#
#         break
#     else:
#         print("Нет такой цифры")
    #
length_banner = float(input("Введите ширину баннера в метрах (например 1.2): ").replace(',', '.'))
whidh_banner = float(input("Введите длину баннера в метрах: ").replace(',', '.'))
pole_for_luvers = input('''Нужно ли прибавить поля для установки люверсов или проклейки?
Введите:
        Да.
        Нет.''').lower()


def dlina(length_banner,whidh_banner):
# делаем длину больше ширины
    if whidh_banner > length_banner:
        length_banner, whidh_banner  = whidh_banner, length_banner
    return length_banner, whidh_banner


# считаем площадь
def S_bannera():
    S = whidh_banner * length_banner
    print('Площадь равна', S, 'кв.м.')

#  прибавляем поля
def pole(whidh_banner, length_banner):
    whidh_banner = whidh_banner + 0.1
    length_banner = length_banner + 0.1
    print('c полями баннер', whidh_banner,"м", 'x', length_banner,"м")
    return whidh_banner, length_banner




# # # подбираем ширину ролика для печати

width_banner_list = [1.1, 1.37, 1.6, 2.2, 2.5, 3.2]
def select_banner():
    if whidh_banner < 3.1:
        for i in range(len(width_banner_list)):
            print("Подбираем ширину из списка", width_banner_list[i])
            if whidh_banner > width_banner_list[i]:
                print("Нужен ролик шире", width_banner_list[i])

            else:
                print("Печатаем на ролике", width_banner_list[i])
                width_banner = width_banner_list[i]
                break
        print("выбран ролик", width_banner, "метра")
        print("Печатаем длинной", length_banner, "метра")
        banner = []
        banner.append(width_banner)
        banner.append(length_banner)
        print(banner)
        # return banner

        # считаем стоимсть печати умножаем ширину ролика на стоимтст прайса
        price_print = price_banner * width_banner * length_banner
        print("Стоимость печати баннера:", round(price_print, 1), "руб.")
        luvers = (width_banner + length_banner)*2*price_luvers
        print("Стоимость установки люверсов", round(luvers,1), "руб.")
        print ("Стоимость баннера длинной", width_banner,"метра", "и шириной", length_banner, "метра с люверсами",round(luvers+price_print,1), "руб.")
    else:
        print("Нужна склейка")


select_banner()

def main():
    dlina(length_banner, whidh_banner) # меняем длину с шириной
    S_bannera()
    if pole_for_luvers == "да":
        pole(dlina(length_banner, whidh_banner))

