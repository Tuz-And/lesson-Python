from random import randint
# Оголосити одновимірний список з 10 елементів типу int.
#  Заповнити його значеннями з клавіатури,
#   вивести на екран та підрахувати добуток
#    елементів списку

# arrau =[]
# i=1
# dobutoc = 1
# while i<=10:
#     num = int(input('введіть елемент'))
#     arrau.append(num)
#     dobutoc *= num
#     i += 1

# print(arrau)
# print(dobutoc)

# 2. Дано список.Заповнити випадковими числами в
#  діапізоні 0 - 20 Знайти суму елементів з
#   непарними індексами.

# arrau =[]
# i=0
# sum = 0
# n= int(input('введіть кількість елементів'))
# while i<n:
#     num = randint(0,20)
#     arrau.append(num)
#     if i%2 == 0 or i==0: sum += num
#     i += 1

# print(arrau)
# print(sum)



# =======================   turle  ===============

import requests


# URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
# currency = requests.get(URL)
# currency = currency.json()
# print("currency ", currency, "\n", type(currency))




# for item in covid19["Countries"]:
#     print(item['Country'])
# print("currency ", currency, "\n", type(currency))



class Covid:
    URL = "https://api.covid19api.com/summary"
    covid19 = requests.get(URL)
    covid19 = covid19.json()

    def getdata(data):
        for item in data["Countries"]:
            print(item['Country'],'\n    NewConfirmed: ',item['NewConfirmed'])
            print('    TotalConfirmed: ',item['TotalConfirmed'],'\n    NewDeaths: ',item['NewDeaths'])
            print('    TotalDeaths:',item['TotalDeaths'],'\n    NewRecovered',item['NewRecovered'])
            print('    TotalRecovered',item['TotalRecovered'],'\n')
    def get_sort(data):
        arrayCountry = []
        arraySort = []

        for item in data["Countries"]:
            array = []
            array.append(item['Country'])
            array.append(item['NewConfirmed'])
            arrayCountry.append(array)
            arraySort.append(item['NewConfirmed'])
            
        arraySort.sort()
        arraySort.reverse()
        for item in arraySort:
            for item2 in arrayCountry:
                if item2[1]==item:
                    print(item2[0],': ',item2[1])
                    arrayCountry.remove(item2)
    def country_info(data):
        nameCountry = input('enter Country')
        for item in data["Countries"]:
            if item['Country']==nameCountry:
                print(item['Country'],'\n    NewConfirmed: ',item['NewConfirmed'])
                print('    TotalConfirmed: ',item['TotalConfirmed'],'\n    NewDeaths: ',item['NewDeaths'])
                print('    TotalDeaths:',item['TotalDeaths'],'\n    NewRecovered',item['NewRecovered'])
                print('    TotalRecovered',item['TotalRecovered'],'\n')
   
    exit = False
    while not exit:
        job = int(
            input(" 1. Show COVID19 information\n2. Sort bt new confirmed\n3. information Country\n0.Exit "))
        if job == 1:
            getdata(covid19)
        elif job==2:
            get_sort(covid19)
        elif job==3:
            country_info(covid19)
        elif job == 0:
            exit=True
        else:
            print("Use --help for reading manual")

