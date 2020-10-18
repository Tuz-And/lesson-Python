import random
from datetime import datetime

if __name__ == "__main__":
    DiscountCard


class DiscountCard:

    def __init__(self):
        self.__account = random.randint(00000000, 99999999)
        self.__discount = 1
        self.__ware = 0
        self.__data = datetime.now().strftime("%d/%m/%y %I:%M")

    def discount_info(self):
        print("DiscountCard: ", self.__account, '\nDiscont: ', self.__discount,
              '%\nPurchases suma:', self.__ware, '\nData: ', self.__data, '\n')

    def purchase(self, ware):
        self.__ware += ware
        self.__discount = self.__ware//1000 + 1
        if self.__discount>15: self.__discount=15
        # print("Purchases suma: ", ware)
        add_purchashe = (self.__ware//1000 + 1)*1000-self.__ware
        amount_due = self.__ware*(100-self.__discount)/100
        print("to increase the discount is still needed: ",
              add_purchashe, "\nAmount due: ", amount_due)
