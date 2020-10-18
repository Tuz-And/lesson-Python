# 1. Скласти програму ’Атракціони’. Програма запитує суму (грн.) у користувача.
#  Потім виводить на екран перелік доступних атракціонів.
# Користувач обирає атракціон та ’оплачує’ його. Вихід з програми при виборі
# пункту ’вихід’ або при недостатній сумі грошей.

# class Attractions:
#     attractions = [
#         ['Оглядове колесо', 30],
#         ['Карусель', 40],
#         ['Тір', 40],
#         ['Каток', 60],
#         ['Боулінг', 90],
#         ['Більярд', 50],
#         ['Картинг', 100]
#     ]

#     many = int(input('Яку суму грошей бажаєте потратити?'))
#     while many >= 0:
#         i = 1
#         print('Ваші гроші', many)

#         for item in attractions:
#             if item[1] <= many:
#                 print(i, '. ', item[0], ': ', item[1])
#             i += 1
#         print('0: Exit')
#         num = int(input('виберіть атракціон за номером'))
#         many = many-attractions[num-1][1]
#         if num == 0:
#             break

#         if many <= 30:
#             print('у вас мало грошей',many)
#             num2 = int(input('1. поповнити баланс\n2. 0 Exit'))
#             if num2 == 0:
#                 break
#             else:
#                 many2 = int(input('внесіть кошти'))
#                 many = many+many2


# 2. Скласти програму ’Банкомат’. Програма запитує пароль
#  (у вигляді числа) у користувача. Якщо пароль вірний, то працює меню з пунктів:
#   поточний баланс, зняти гроші, вихід.

class CashMachine:
    balance = 3000
    passvord = 1111
    i = 0
    exit = False
    while not exit:
        num = int(input('введіть пароль'))
        if num != passvord:
            print('невірний пароль')
            i += 1
            if i == 3:
                print('карточку забрав банкомат!!!!!!!!!!!!! :-)')
                break
        else:
            operation = int(input('1.Поточний баланс\n2.Зняти гроші\n0.Exit'))
            if operation == 1:
                print('ваш баланс', balance)
            elif operation == 2:
                money = int(input('введіть суму яку бажаєте зняти: '))
                if money > balance:
                    print('недостатньо грошей на рахунку')
                    continue
                if money < 0:
                    print('невірно вказана сума')
                    continue
                balance -= money
            else:
                break
