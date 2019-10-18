# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth
 description To P_r9 Ethernet0/2


Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''

# Solution

import re

def get_ints_without_description(filename):
    with open(filename, 'r') as config:
        regex_without_desc = (r'(?P<iface>interface\s\w+/?\d+\n\sip)')
        regex_iface= (r'(?P<iface>interface\s\w+/?\d+)')
        ifaces = re.findall(regex_without_desc, config.read())
        intf_list = []
        if ifaces:
            for element in ifaces:
                iface = re.search(regex_iface, element)
                intf_list.append(iface.group(0))
        
    print(intf_list)

get_ints_without_description('config_r1.txt')





