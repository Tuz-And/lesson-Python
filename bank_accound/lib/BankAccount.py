import random

if __name__ == "__main__":
    BankAccount


class BankAccount:
    def __init__(self, currency: str, start_cashe: int):
        self.__currency = currency
        self.__account = random.randint(00000000, 99999999)
        self.__start_cashe = start_cashe

    def account_info(self):
        print('Account: ', self.__account, '\nCurrency: ',
              self.__currency, '\nCashe: ', self.__start_cashe)

    def remove_from_account(self, cashe: int):
        if cashe<0:
            print('Error suma')
        elif cashe==0:
            print('you enter null')
        else:
            self.__start_cashe -= cashe

    def add_from_account(self, cashe: int):
        if cashe<0:
            print('Error suma')
        elif cashe==0:
            print('you enter null')
        else:
            self.__start_cashe += cashe
