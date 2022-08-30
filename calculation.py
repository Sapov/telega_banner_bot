import data
from data import material_banner


# noinspection PyUnreachableCode
def calculation(material_name, whidth_material=1, higth_material=3, pole_for_luvers=False):
    '''

    :param material_name: Имя материала к примеру 440 баннер
    :param whidth_material: Ширина материала
    :param higth_material: Длина материаоа
    :param pole_for_luvers: Отметка нужно ли поле для люверсов
    :return: стоимость печати
    '''


    global whidth_roll
    if whidth_material > higth_material:
        whidth_material, higth_material = higth_material, whidth_material # длина всегда больше ширины
    print(f' ширина печати {whidth_material}m а длина: {higth_material}m')
    if pole_for_luvers:  # если нужно поле под люверсы добавляем по 5 см с каждой стороны
        higth_material = higth_material + 0.1
        whidth_material += 0.1
        print(f' Размер печати с полями  имеет размер {higth_material} x {whidth_material}')
        # print(material_name)
    # Сравниваем ширины роликов баннера 440 грамм
    width_banner_roll = material_banner[material_name][1]
    for i in width_banner_roll:
        if whidth_material <= material_banner[material_name][1][-1]: # максимальная ширина ролика а потом склейка
            print(f' Максимальный ролик>>>{material_banner[material_name][1][-1]}')


            if whidth_material > i-0.06: # берем размеры минус 6 см чтоб не печатать в край
                print(f' new roll')
            else:

                whidth_roll = i
                print(f' ставим ролик = {whidth_roll}')
                #break

                price_material = material_banner[material_name][0]
                print(f' Стоимость печати 1 м2: {price_material} руб.')
                square_print = round(whidth_roll * higth_material, 1)
                price = round(price_material * square_print,1)
                luvers_work = round((higth_material*whidth_material)*data.price_luvers*2,1)
                print(f' Площадь печати {square_print}m2')
                print(f' Напечатать на материале {material_name} стоит {price} руб.')
                print(f' Поставить люверсы стоит {luvers_work}руб.')
                print(f' Итого стоимость материала с установкой люверсов: {luvers_work+price}руб.')
                return price
    else:
        print("Требуется склейка")



# calculation("Баннер 440 грамм", 3, 0.8, True)
