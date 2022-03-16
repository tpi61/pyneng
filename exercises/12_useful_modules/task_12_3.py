# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

from task_12_1 import ping_ip_addresses
from tabulate import tabulate

ip_list = ['192.168.56.10', '8.8.8.8', '99.99.99.99','a']


def print_ip_table(reachable, unreachable):
    new_dict = {'Reachable' : reachable, 'Unreachable' : unreachable}
    print(tabulate(new_dict, headers='keys'))

print_ip_table(ping_ip_addresses(ip_list)[0], ping_ip_addresses(ip_list)[1])


# ANSWER
############################
# from tabulate import tabulate


# def print_ip_table(reach_ip, unreach_ip):
#     table = {"Reachable": reach_ip, "Unreachable": unreach_ip}
#     print(tabulate(table, headers="keys"))


# if __name__ == "__main__":
#     reach_ip = ["10.1.1.1", "10.1.1.2"]
#     unreach_ip = ["10.1.1.7", "10.1.1.8", "10.1.1.9"]
#     print_ip_table(reach_ip, unreach_ip)
