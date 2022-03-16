# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess

def ping_ip_addresses(list_of_ip_add):
    avaliable_ip = []
    unavaliable_ip = []
    for ip in list_of_ip_add:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                encoding='utf-8')
        if reply.returncode == 0:
            avaliable_ip.append(ip)
        else:
            unavaliable_ip.append(ip)
    return avaliable_ip, unavaliable_ip


#print(ping_ip_addresses(['192.168.56.10','192.168.56.1','8.8.8.8','a']))

# ANSWER
########################################
# import subprocess


# def ping_ip_addresses(ip_addresses):
#     reachable = []
#     unreachable = []

#     for ip in ip_addresses:
#         result = subprocess.run(
#             ["ping", "-c", "3", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE
#         )
#         if result.returncode == 0:
#             reachable.append(ip)
#         else:
#             unreachable.append(ip)

#     return reachable, unreachable


# if __name__ == "__main__":
#     print(ping_ip_addresses(["10.1.1.1", "8.8.8.8"]))