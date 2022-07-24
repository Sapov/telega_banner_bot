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
            До 6 м2 считается по цене к примеру 350 руб./м2 после 280 руб./м2 для 440 баннера
            вывод стоимости баннера
4.2. Печать на пленке
4.3. Печать на бумаге
4.4. Печать на сетке
4.5. Печать на перфопленка
4.6. Печать на Фотообои"""

from data import *

from raschet import main
import pyinputplus as pyip
def change_material():
    change_material = pyip.inputMenu(list(fist_change_material_1), numbered=True)
    if change_material == "Печать на баннере":
        variant = pyip.inputMenu(list(banner), numbered=True)
        if variant == "Баннер 440 грамм":
            main(banner["Баннер 440 грамм"])
        elif variant == "Баннер 330 грамм":
            main(banner["Баннер 330 грамм"])
        elif variant == "Баннер 510 грамм (литой)":
            main(banner["Баннер 510 грамм (литой)"])
    elif change_material=="Печать на сетке":
        main(setka["Баннерная сетка"])
    elif change_material=="Печать на пленке":
        variant = pyip.inputMenu(list(film), numbered=True)
    elif change_material=="Печать на перфопленке":
        main(perfo_film["Перфорированная пленка"])
    elif change_material=="Печать на бумаге":
        variant = pyip.inputMenu(list(paper), numbered=True)
        if variant == "Бумага blueback":
            main(paper["Бумага blueback"])
        elif variant == "Бумага CityLight 150 грамм":
            main(paper["Бумага CityLight 150 грамм"])
    elif change_material=="Печать на фотообоях":
        main(data.fotooboi["Фотообои"])

####
change_material()