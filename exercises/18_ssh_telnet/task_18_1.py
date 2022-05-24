# -*- coding: utf-8 -*-
"""
Задание 18.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к ОДНОМУ устройству
и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml
с помощью функции send_show_command (эта часть кода написана).

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
            for command in commands:
                output = ssh.send_command(command)
                result[command] = output
        return result
    except (NetmikoAuthenticationException):
        print('Неверный логин или пароль')
    except (NetmikoTimeoutException) as error:
        print(error)
    
if __name__ == "__main__":
    commands = ["sh ip int br"] # must be list
    with open("devices2.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        pprint(send_show_command(dev, commands), width=120)



