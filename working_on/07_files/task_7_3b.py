# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

result = []
with open('CAM_table.txt', 'r') as mac:
    for line in mac:
        if 'DYNAMIC' in line:    
            current_line = line.split()
            current_line[0]=int(current_line[0])
            #result.append('{0:<5} {1:16} {2:10}'.format(vid, a[1], a[3]))
            #macaddr = current_line[1]
            #intf = current_line[3]
            result.append(current_line)

answer = int(input('Enter vlan-id: '))

for line in sorted(result):
    if line[0] == answer:
        print(f'{line[0]:<5}   {line[1]:15}    {line[3]:10}') 