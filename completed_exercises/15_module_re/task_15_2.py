# -*- coding: utf-8 -*-
'''
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

'''

# Solution

import re

def parse_sh_ip_int_br(filename):
    #regex = (r'(?P<iface>[A-Za-z]+[0-9]+\/[0-9]+|[A-Za-z]+[0-9]+)\s+(?P<ip>\d+\.\d+\.\d+\.\d+|[a-z]+)\s+[A-Z]+\s+[a-z]+\s+(?P<status>[a-z]+\s?[a-z]+)\s+(?P<protocol_state>[a-z]+)')
    regex = (r'(?P<iface>\w+/?\d+)\s+(?P<ip>\d+\.\d+\.\d+\.\d+|[a-z]+)\s+\w+\s+\w+\s+(?P<status>\w+\s?\w+)\s+(?P<protocol_state>\w+)')
    with open(filename, 'r') as f:
        IP_LIST = re.findall(regex, f.read())

    #print(IP_LIST)
    return IP_LIST

parse_sh_ip_int_br('sh_ip_int_br.txt')