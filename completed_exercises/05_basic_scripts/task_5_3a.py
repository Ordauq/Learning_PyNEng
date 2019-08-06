# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'Введите номер VLAN: ',
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'Введите разрешенные VLANы: ',
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

# Solution
#dict_portmode = dict([('access', access_template), ('trunk', trunk_template)])
dict_portmode = {'access': access_template, 'trunk': trunk_template}

port_mode = input('Введите режим работы интерфейса (access/trunk): ')
iface = input('Введите тип и номер интерфейса: ')


print(dict_portmode[port_mode][0])
vlan_id = input('')

del dict_portmode[port_mode][0]
print('interface', iface)
to_print = '\n'.join(dict_portmode[port_mode])
print(to_print.format(vlan_id))