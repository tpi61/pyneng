# -*- coding: utf-8 -*-
"""
Задание 18.1a

Скопировать функцию send_show_command из задания 18.1 и переделать ее таким образом,
чтобы обрабатывалось исключение, которое генерируется при ошибке аутентификации
на устройстве.

При возникновении ошибки, на стандартный поток вывода должно выводиться
сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
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
    # except (NetmikoAuthenticationException) as error:
    #     print(error)
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        return error
    
if __name__ == "__main__":
    commands = ["sh ip int br"] # must be list
    with open("devices2.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        pprint(send_show_command(dev, commands), width=120)