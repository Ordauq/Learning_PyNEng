# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

# Solution
import sys


with open(sys.argv[1], 'r') as config, open('config_sw1_cleared.txt', 'w') as dst:
    for line in config:
        #counter = 0
        if line.startswith('!'):
            pass
        else:
            counter = 0
            for word in ignore:
                if word in line:
                    counter +=1
                    break
            if counter == 0:
                dst.write(line)
            else:
                pass