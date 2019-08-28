# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['Current configuration', 'duplex', 'alias']
# Solution
import sys


with open(sys.argv[1], 'r') as config:
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
                print(line.rstrip())
            else:
                pass