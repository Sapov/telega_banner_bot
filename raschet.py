banner = {"Баннер 440 грамм": "350",
          "Баннер 330 грамм": "300",
          "Баннер 510 грамм (литой)": "400"}
film = {"Пленка orajet_3640 белая матовая": "450",
        "Пленка orajet_3640 белая Глянцвая": "450",
        "Пленка Orajet_3640 прозрачная Глянцвая": "450",
        "Пленка Orajet_3640 прозрачная Матовая": "450",
                    "Пленка Китай белая матовая": "375",
        "Пленка Китай белая глянцевая": "375",
        "Пленка Китай прозрачная матовая": "375",
        "Пленка Китай прозрчная глянцевая": "375"}
setka = {"Баннерная сетка": "275"}
perfo_film = {"Перфорированная пленка": "650"}
paper = {"Бумага blueback": "90",  "Бумага CityLight 150 грамм": "220"}
fotooboi = {"Фотообои": "950"}
fist_change_material =["Баннер", "Пленка", "Бумага", "Показать все возможные материалы"]

price_banner = 350 # руб. за 1 метр
price_luvers = 120 # рую. за 1 метр погонный


# ----- функция перебираеем словарь  и вывдим в менюшку

def print_menu(dic_material):
    print("Введите номер для выбора типа материала:".center(100, "-"))
    index_b = 0
    materials = []
    for k in dic_material.keys():
        index_b += 1
        print(f'{index_b}.{k}')
        materials.append(k)

    print("Введите номер для выбора".center(100,"="))
    while True:
        numer_material = input("Введите цифру: ")
        ### проверяем если numer_material равен цифре -1 и не больше чем len(materials)
        if numer_material == "1" and float(numer_material) <= len(materials):
            print("Считаем", materials[0])
            break
        elif numer_material == "2" and float(numer_material) <= len(materials):
            print("Считаем", materials[2-1])
            break
        elif numer_material == "3" and float(numer_material) <= len(materials):
            print("Считаем", materials[2])
            break
        else:
            print("Введите правильную цифру")

print(" Выбираем материал для широкоформатной печати: ".center(100,"*") + "\n" "Введите номер для выбора типа материала:")
index_1 = 0
for item in range(len(fist_change_material)):
    index_1 +=1
    print(f'{index_1}. {fist_change_material[item]}')

while True:
    number_material = input("Введите номер: ")
    if number_material == "4":
        for k in price_material.keys():
            print(k)

            break
    elif number_material == "1":
        # print('\n')
        # ----- функция перебираеем словарь  и вывдим в менюшку
        print_menu(banner)

        break


    elif number_material == "2":
        print("Fim")
        print_menu(film)

        break
    elif number_material == "3":
        print("Paper")
        print_menu(paper)

        break
    else:
        print("Нет такой цифры")
        # continue
    #
length_banner = float(input("Введите ширину баннера в метрах (например 1.2): ").replace(',', '.'))
whidh_banner = float(input("Введите длину баннера в метрах: ").replace(',', '.'))
def dlina(length_banner,whidh_banner):
    # делаем длину больше ширины
    if whidh_banner > length_banner:
        length_banner, whidh_banner  = whidh_banner, length_banner

dlina(length_banner,whidh_banner)

# считаем площадь
def S_bannera():
    S = whidh_banner * length_banner
    print('Площадь равна', S, 'кв.м.')

S_bannera()

#  прибавляем поля
def pole():
    global whidh_banner, length_banner
    whidh_banner = whidh_banner + 0.1
    length_banner = length_banner + 0.1
    print('c полями баннер', whidh_banner,"м" 'x', length_banner,"м")
pole()


# считаем стоимость печати баннера + пустые поля по цене материала (цена материала это закупочная стоимость х 1.8)
print('размер баннера: ', whidh_banner)

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


