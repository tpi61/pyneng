# -*- coding: utf-8 -*-
"""
Задание 18.2a

Скопировать функцию send_config_commands из задания 18.2 и добавить параметр log,
который контролирует будет ли выводится на стандартный поток вывода информация о том
к какому устройству выполняется подключение.
По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, log=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства
из файла devices.yaml с помощью функции send_config_commands.
"""


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
            print('Connecting to ' + hostname + '...  Ip is ' + dev['host'])
            output = ssh.send_config_set(commands)
        return output
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
         return error
    
if __name__ == "__main__":
    commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']  # must be list
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        pprint(send_show_command(dev, commands))