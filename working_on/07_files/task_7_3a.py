# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#Solution 
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


for line in sorted(result):
        print(f'{line[0]:<5}   {line[1]:15}    {line[3]:10}') 