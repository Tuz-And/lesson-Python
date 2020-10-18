# 1. Написати клас "Карточка на знижку" (DiscountCard),
# який містить наступну інформацію:

# Номер карточки
# Розмір знижки (знижка передбачається накопичуваною;
#   на початковому етапі вона рівна 1%. За кожні 1000 грн. покупки,
#   сума знижки збільшується на 1%.)
# Приховане допоміжне поле для збереження вартості накупленого товару
# Дата видачі карточки в форматі "12/02/1200")
# Забезпечити можливість:
# Купляти товар з використанням карточки на знижку;
# Виводити інформацію про поточну величину знижки;
# Виводити інформацію про те, на яку суму ще необхідно докупити товару,
#  щоб величина знижки збільшилась.

from lib.DiscountCard import DiscountCard

dicon = DiscountCard()


a = False
while not a:
    try:
        sum = int(input('enter the purchase amount'))
        dicon.purchase(sum)
        dicon.discount_info()
        num = int(input("***********\n1.continue shopping\n2.to pay"))
    
        if num == 2:
            print("Thank you for your purchase")
            a = True
    except ValueError:
        print("incorrectly entered data")


