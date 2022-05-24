# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    with open(config_filename) as f:
        dict_access = {}
        dict_trunk = {}
        adopted_config = []
        for line in f:
            if not line.startswith("!") and "interface Fast" in line or "switchport access vlan" in line or "switchport trunk allowed" in line:
                adopted_config.append(line.rstrip())
        adopted_config = ''.join(adopted_config).split('interface ')
        for line in adopted_config:
            if 'Ethernet' in line and 'switchport access' in line:
                acc_line = line.split()
                dict_access[acc_line[0]] = int(acc_line[-1])
            elif 'Ethernet' in line and 'trunk allowed' in line:
                trunk_line = line.split()
                dict_trunk[trunk_line[0]] = [int(vl) for vl in trunk_line[-1].split(',')]
                #print(trunk_line)
        result = []
        result.append(dict_access)
        result.append(dict_trunk)
        #print(tuple(result))
        return tuple(result)

get_int_vlan_map('config_sw1.txt')

# ANSWER
###################################
def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}

    with open(config_filename) as cfg:
        for line in cfg:
            line = line.rstrip()
            if line.startswith("interface"):
                intf = line.split()[1]
            elif "access vlan" in line:
                access_dict[intf] = int(line.split()[-1])
            elif "trunk allowed" in line:
                trunk_dict[intf] = [int(v) for v in line.split()[-1].split(",")]
        return access_dict, trunk_dict