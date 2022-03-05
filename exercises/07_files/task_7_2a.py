# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv

filename = argv[1]

with open(filename) as f:
    for line in f:
        if not line.startswith("!") and ignore[0] not in line and ignore[1] not in line and ignore[2] not in line:
            print(line.rstrip())

# # ANSWER
# from sys import argv

# ignore = ["duplex", "alias", "configuration"]

# filename = argv[1]

# with open(filename) as f:
#     for line in f:
#         words = line.split()
#         words_intersect = set(words) & set(ignore)
#         if not line.startswith("!") and not words_intersect:
#             print(line.rstrip())