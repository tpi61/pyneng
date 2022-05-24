# -*- coding: utf-8 -*-
"""
Задание 18.2

Создать функцию send_config_commands

Функция подключается по SSH (с помощью netmiko) к ОДНОМУ устройству и выполняет
перечень команд в конфигурационном режиме на основании переданных аргументов.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* config_commands - список команд, которые надо выполнить

Функция возвращает строку с результатами выполнения команды:

In [7]: r1
Out[7]:
{'device_type': 'cisco_ios',
 'ip': '192.168.100.1',
 'username': 'cisco',
 'password': 'cisco',
 'secret': 'cisco'}

In [8]: commands
Out[8]: ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']

In [9]: result = send_config_commands(r1, commands)

In [10]: result
Out[10]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.
         \nR1(config)#logging 10.255.255.1\nR1(config)#logging buffered 20010\n
         R1(config)#no logging console\nR1(config)#end\nR1#'

In [11]: print(result)
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 10.255.255.1
R1(config)#logging buffered 20010
R1(config)#no logging console
R1(config)#end
R1#


Скрипт должен отправлять команду command на все устройства из файла devices.yaml
с помощью функции send_config_commands.
"""

# commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
# -*- coding: utf-8 -*-


from pprint import pprint

import yaml
from netmiko import (ConnectHandler, NetmikoAuthenticationException,
                     NetmikoTimeoutException)


def send_show_command(dev, commands):
    result = {}
    try:
        with ConnectHandler(**dev) as ssh:
            ssh.enable()
            hostname = ssh.find_prompt().rstrip('#')
            print('Connecting to ' + hostname + '...')
            #for command in commands:
            output = ssh.send_config_set(commands)
    #         result[ssh[host]] = output
        return output
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
         return error
    
if __name__ == "__main__":
    commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']  # must be list
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        pprint(send_show_command(dev, commands))