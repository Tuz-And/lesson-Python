# 1. Написати додаток який буде звертатись в кожні 30-60 сек
#  на https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5
# і записувати в файл  відповіді від сервера в форматі:
#  | username | час та дата | відповідь від сервера
# відповіді успіху записувати в файл access.log невдач в error.log


import requests
import random
import datetime
import time

import platform


class PrivatError:
    URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    a = False
    today = datetime.datetime.today()
    while not a:
        try:
            error_file = open("error.log", "a")
            myhost = platform.uname().node
            date = today.strftime('%Y-%m-%d-%H:%M:%S')
            access_file = open("access.log", "a")
            response = str(requests.get(URL))
            access_file.write("| "+myhost+" | "+date+" | "+response+"\n")
            print("| "+myhost+" | "+date+" | "+response+"\n")

        except:

            error_file.write("| "+myhost+" | "+date+" | "+response+"\n")

        finally:
            access_file.close()
            error_file.close()

        pause = random.randint(30, 60)
        time.sleep(pause)

        # except httplib2.ServerNotFoundError:
        #     print('Сервер недоступен, повторное подключение')
        # except ConnectionRefusedError:
        #     print('Соединение разорвано, повторное подключение')
        # except httplib2.socket.timeout:
        #     print('Таймаут запроса, повторное подключение')
        # except OSError:
        #     print('Нету подключения к сети, ожидание 60 секунд')
