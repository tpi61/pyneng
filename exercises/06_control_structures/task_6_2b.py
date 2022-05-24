# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

valid_ip = False

while not valid_ip:
    ip = input("Введите IP-адрес в формате x.x.x.x: ")
    octets = ip.split(".")
    valid_ip = len(octets) == 4

    for i in octets:
        valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip

    if valid_ip:
        if 1 <= int(octets[0]) <= 223:
            print("unicast")
        elif 224 <= int(octets[0]) <= 239:
            print("multicast")
        elif ip == "255.255.255.255":
            print("local broadcast")
        elif ip == "0.0.0.0":
            print("unassigned")
        else:
            print("unused")
    else:
        print("Неправильный IP-адрес")
        