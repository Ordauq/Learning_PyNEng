# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

# Solution
def get_int_vlan_map(config_filename):
    '''
    config_filename - файл с конфигом интерефейсов (cisco-like)

    Возвращает кортеж из двух словарей (для access и для trunk-портов)
    '''
    with open(config_filename, 'r') as config:
        interface_access = {}
        interface_trunk = {}
        for line in config:
            if line.startswith('interface'):
                iface = line.split()[-1].rstrip()
            if 'switchport access vlan' in line:
                vlan = line.split()[-1].rstrip()
                interface_access[iface] = vlan
            elif 'switchport trunk allowed vlan' in line:
                vlan = (line.split()[-1].rstrip().split(','))
                for vid in vlan:
                    interface_trunk.setdefault(iface, []).append(int(vid))


    return (interface_access, interface_trunk)

for i in get_int_vlan_map('config_sw1.txt'):
    print(i)