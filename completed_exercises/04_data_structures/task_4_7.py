# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

original = '101010101010101010111011101110111100110011001100'
mac = 'AAAA:BBBB:CCCC'
mac = int(mac.replace(':', ''), 16)
mac = bin(mac)
mac = str(mac).lstrip('0b')

print(original == mac)