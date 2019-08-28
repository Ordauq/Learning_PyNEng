# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

# Solution
import sys


with open(sys.argv[1], 'r') as config, open(sys.argv[2], 'w') as dst:
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