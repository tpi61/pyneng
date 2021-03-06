# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

from turtle import clear


mac = "AAAA:BBBB:CCCC"

#split_mac = mac.split(':')
#oct_1 = str(bin(int(split_mac[0], 16)))
#oct_2 = str(bin(int(split_mac[1], 16)))
#oct_3 = str(bin(int(split_mac[2], 16)))
#
#bit_mac = oct_1[2:] + oct_2[2:] + oct_3[2:]

bit_mac = '{:b}'.format(int(mac.replace(':', ''), 16))

print(bit_mac)