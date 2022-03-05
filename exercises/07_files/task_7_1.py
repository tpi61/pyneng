# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


with open('ospf.txt') as f:
    for line in f:
#        print(line.split())
        print('{:22}{}'.format('Prefix', line.split()[1]))
        print('{:22}{}'.format('AD/Metric', line.split()[2].strip('[]')))
        print('{:22}{}'.format('Next-Hop', line.split()[4].rstrip(',')))
        print('{:22}{}'.format('Last update', line.split()[-2].rstrip(',')))
        print('{:22}{}'.format('Outbound Interface', line.split()[-1]))
        print("")

# ANSWER
# ####################################
# output = "\n{:25} {}" * 5

# # with open("ospf.txt", "r") as f:
# #     for line in f:
# #         route = line.replace(",", " ").replace("[", "").replace("]", "")
# #         route = route.split()

# #         print(output.format(
# #                 "Prefix", route[1],
# #                 "AD/Metric", route[2],
# #                 "Next-Hop", route[4],
# #                 "Last update", route[5],
# #                 "Outbound Interface", route[6],
# #         ))