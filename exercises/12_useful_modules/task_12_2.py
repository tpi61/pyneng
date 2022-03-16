# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
def convert_ranges_to_ip_list(ip_add_list):
    result = []
    for ip in ip_add_list:
        if len(ip.split('.')) == 4 and not '-' in ip:
            result.append(ip)
        elif '-' in ip and len(ip.split('.')) > 6:
            temp_ip = ip.split('-')
            start_range = int(temp_ip[0].split('.')[-1])
            end_range = int(temp_ip[1].split('.')[-1]) + 1
            ip_string = '.'.join(temp_ip[0].split('.')[0:3]) + '.'
            for n in range(start_range, end_range):
                result.append(ip_string + str(n))
        elif '-' in ip and len(ip.split('.')) == 4:
            temp_ip = ip.split('-')
            start_range = int(temp_ip[0].split('.')[-1])
            end_range = int(temp_ip[1].split('.')[-1]) + 1
            ip_string = '.'.join(temp_ip[0].split('.')[0:3]) + '.'
            for n in range(start_range, end_range):
                result.append(ip_string + str(n))
        

    return result
print(convert_ranges_to_ip_list(['192.168.56.10', '88.8.8.8-88.8.8.9','10.0.0.1-5']))


# ANSWER
####################################
# import ipaddress


# def convert_ranges_to_ip_list(ip_addresses):
#     ip_list = []
#     for ip_address in ip_addresses:
#         if "-" in ip_address:
#             start_ip, stop_ip = ip_address.split("-")
#             if "." not in stop_ip:
#                 stop_ip = ".".join(start_ip.split(".")[:-1] + [stop_ip])
#             start_ip = ipaddress.ip_address(start_ip)
#             stop_ip = ipaddress.ip_address(stop_ip)
#             for ip in range(int(start_ip), int(stop_ip) + 1):
#                 ip_list.append(str(ipaddress.ip_address(ip)))
#         else:
#             ip_list.append(str(ip_address))
#     return ip_list