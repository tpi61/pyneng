# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""

# import re
# def get_ip_from_cfg(config): 
#     regex = (r'interface (?P<intf>\S+)'
#              r'|ip address (?P<ipadd>\S+) (?P<mask>\S+)')
#     result = {}
#     with open(config) as f:
#         iter = re.finditer(regex, f.read())
#         for line in iter:
#           if line.lastgroup == 'intf':
#             intf = line.group(line.lastgroup)
#             result[intf] = ()
#           else:
#             result[intf] = line.group('ipadd', 'mask')
#         for key in list(result.keys()):
#           if len(result[key]) < 1:
#             del result[key]        
#     return result

# get_ip_from_cfg('config_r1.txt')

# answer
# #########
import re

def get_ip_from_cfg(config):
    with open(config) as f:
        regex = re.compile(
            r"interface (?P<intf>\S+)\n"
            r"( .*\n)*"
            r" ip address (?P<ip>\S+) (?P<mask>\S+)"
        )
        match = regex.finditer(f.read())

    result = {m.group("intf"): m.group("ip", "mask") for m in match}
    return print(result)

get_ip_from_cfg('config_r1.txt')