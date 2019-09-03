# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
            elif 'switchport mode access' in line:
                vlan = '1'
                interface_access[iface] = vlan
            elif 'switchport trunk allowed vlan' in line:
                vlan = (line.split()[-1].rstrip().split(','))
                for vid in vlan:
                    interface_trunk.setdefault(iface, []).append(int(vid))


    return (interface_access, interface_trunk)

for i in get_int_vlan_map('config_sw2.txt'):
    print(i)