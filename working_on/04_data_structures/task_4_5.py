# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

# Solution
vlans1 = command1[(command1.find('1')):]
vlans2 = command2[(command2.find('1')):]
vlans_list1 = set(sorted(vlans1.split(',')))
vlans_list2 = set(sorted(vlans2.split(',')))
result = list(vlans_list1 & vlans_list2)
print(result)