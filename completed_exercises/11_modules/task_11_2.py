# -*- coding: utf-8 -*-
'''
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''

# Solution

import draw_network_graph as dr

def readfile(file):
        with open(file, 'r') as config:
            return config.read()

def parse_cdp_neighbors(command_output):
    command_output = command_output.strip().split('\n')
    device_dict = {}
    for line in command_output:
        if 'show cdp neighbors' in line:
            device_id = line[0:line.find('>')]
        if 'Eth' in line:
            line = line.split()
            key = (device_id, line[1]+line[2])
            value = (line[0], line[-2]+line[-1])
            device_dict.update({key: value})
    
    return device_dict

def create_network_map(filenames):
    topology_dict = {}
    for file in filenames:
        current_file = readfile(file)
        topology_dict.update(parse_cdp_neighbors(current_file))
    
    great_fucking_topology = {}
    tmpDict = topology_dict.copy()
    for k in tmpDict.keys():
        for v in tmpDict.values():
            if k[0] == v[0]:
                if k == v:
                    pass
                else:
                    great_fucking_topology.update({k : tmpDict.get(k)})

    return great_fucking_topology

#print(create_network_map(['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']))
dr.draw_topology(create_network_map(['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']))