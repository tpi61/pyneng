# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
mac_list = []

with open('CAM_table.txt') as f:
    for line in f:
        split_line = line.split()
        if split_line and split_line[0].isdigit():
            vlan, mac, _, intf = split_line
            mac_list.append([int(vlan),mac,intf])

chosen_vlan = int(input('Please enter VLAN number: '))

for vlan, mac, intf in sorted(mac_list):
    if chosen_vlan == vlan:
        print(f"{vlan:<9}{mac:20}{intf}")
        