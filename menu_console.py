""" 1. сначала спрашиваем кто считает заказчик или рекламное агенство
проверка по id розничного заказчика и РА
2. широкоформатная печать или интерьерная
3. широкоформатная:
4.1. Печать на баннере:
    ПРИ НАЖАТИИ - Выводим все плотности баннера
    510 грамм
    410 грамм
    310 грамм
        Уточняем выпуски для люверсов
        Ставим ли люверсы
        Проклейка без люверсов
        Проклейка кармана под трубу
            До 6 м2 считается по цене к примеру 350 руб./м2,
             после 280 руб./м2 для 440 баннера
            вывод стоимости баннера
4.2. Печать на сетке (СЕТКА СУЩЕСТВУЕТ ТОЛЬКО РАЗМЕРОМ 3.2 М)
4.3. Печать на бумаге (У БУМАГИ РАЗМЕР 1.25)
4.4. Печать на пленке (РАЗМЕР 1.05, 1.26. 1,37. 1.52)
4.5. Печать на перфопленка (1 и 1.37)
4.6. Печать на Фотообои ШИРИНА 1МЕТР''' """
import calculation
from raschet import main
import pyinputplus as pyip
from data import *


def razmer(pole=True):
    '''Запрашиваем размеры Материала" и спрашиваем нужно ли поле для люверсов
    length_banner - Длина баннера
    whidh_banner - Ширина баннера'''
    length_banner = pyip.inputFloat("Введите ширину печати в метрах: ")
    whidh_banner = pyip.inputFloat("Введите длину печати в метрах: ")
    if pole: # считаем  поле если есть параметр поле
        pole_for_luvers = pyip.inputYesNo('''Нужно ли прибавить поля для установки люверсов или проклейки?
        Введите:
                 Да.
                 Нет. : ''', yesVal="да", noVal='нет')
        print(pole_for_luvers)
    else:
        pole_for_luvers = False

    return length_banner, whidh_banner, pole_for_luvers


def change_material():
    """ Выводим менюшку для выбора материла для печати
    -- передаем в расчет
    Длину, ширину, стоимость за 1 м2 и имя материала для расчета по ширине ролика"""
    change_material = pyip.inputMenu(list(fist_change_material), numbered=True)
    if change_material == "Печать на баннере":
        variant = pyip.inputMenu(list(banner), numbered=True)
        if variant == "Баннер 440 грамм":

            calculation.calculation(variant, *razmer())

        elif variant == "Баннер 330 грамм":
            # main(*(razmer() + ("Баннер 330 грамм",)))
            calculation.calculation(variant, *razmer())

        elif variant == "Баннер 510 грамм (литой)":
            calculation.calculation(variant, *razmer())
    elif change_material == "Печать на сетке":
        calculation.calculation(change_material, *razmer())


    elif change_material == "Печать на пленке":
        variant = pyip.inputMenu(list(material_film), numbered=True)# если razmer(False)значит для материала не нужно поле и люверсы
        if variant == 'Пленка orajet_3640 белая матовая':
            calculation.calculation(variant, *razmer(False))
        elif variant == 'Пленка orajet_3640 белая Глянцвая':
            calculation.calculation(variant, *razmer(False))
        elif variant == 'Пленка Orajet_3640 прозрачная Глянцвая':
            calculation.calculation(variant, *razmer(False))
        elif variant == 'Пленка Orajet_3640 прозрачная Матовая':
            calculation.calculation(variant, *razmer(False))
        elif variant == 'Пленка Китай белая матовая':
            calculation.calculation(variant, *razmer(False))
        elif variant == 'Пленка Китай белая глянцевая':
            calculation.calculation(variant, *razmer(False))
        elif variant == 'Пленка Китай прозрачная матовая':
            calculation.calculation(variant, *razmer(False))
        elif variant == 'Пленка Китай прозрчная глянцевая':
            calculation.calculation(variant, *razmer(False))


    elif change_material == "Печать на перфопленке":
        calculation.calculation(change_material, *razmer(False))

    elif change_material == "Печать на бумаге":
        variant = pyip.inputMenu(list(material_paper), numbered=True)
        if variant == "Бумага blueback":
            calculation.calculation(variant, *razmer(False))
        elif variant == "Бумага CityLight 150 грамм":
            calculation.calculation(variant, *razmer(False))

    elif change_material == "Печать на фотообоях":
        calculation.calculation(change_material, *razmer(False))


####
change_material()
