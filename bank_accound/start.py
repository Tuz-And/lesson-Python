# Написати клас "Банківський рахунок" (Account), який містить:
# Номер рахункуРозмір коштів на рахункуНазва валюти рахунку
# (рублі, гривні, евро тощо), для позначення якої можна
# скористатись одним символом: R, G, E, $ тощо
# Забезпечити можливість:
# Відкривати рахунок та первинно вносити гроші на рахунокЗнімати
# гроші з рахункуДокладати гроші на рахунок
# ПРИМІТКА! На 12 балів реалізувати також можливість здійснювати
# переказ грошей з одного рахунку на другий.

from lib.BankAccount import BankAccount

account = BankAccount('ua', 15000)
# account1.remove_from_account(5000)
# account1.account_info()
# print('===================')
# account1.add_from_account(7000)
# account1.account_info()

flag = False

while not flag:
    num = int(
        input("Write number menu: \n  1.Enter in account \n  2.Create account\n  0.Exit"))
    if num == 1:
        num2 = int(
            input("Write number menu: \n  1.Remove cashe\n  2.Add cashe\n  0.Exit"))
        if num2 == 1:
            account.remove_from_account(int(input('enter suma')))
        elif num2 == 2:
            account.add_from_account(int(input('enter suma')))
        else:
            break
        account.account_info()
    elif num==2:
        curency = input('enter curency: ')
        sum = int(input('enter suma'))
        account1 = BankAccount(curency,sum)
        account1.account_info()
    else:
        break

    

