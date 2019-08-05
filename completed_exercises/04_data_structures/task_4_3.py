# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки config список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'

# Solution
new_config = config.split()
vlans = new_config[4]
vlans_list = vlans.split(',')
print(vlans_list)

# Solution #2
new_config = config[30:] #found start of slicicng with my own hands :)
vlans_list = new_config.split(',')
print(vlans_list)

# Solution #3
new_config = config[(config.find('1')):]
vlans_list = new_config.split(',')
print(vlans_list)