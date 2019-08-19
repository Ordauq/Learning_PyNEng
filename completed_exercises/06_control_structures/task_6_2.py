# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

# Solution
try:
    ip_addr = input('Hello. Please enter IP address in format x.x.x.x: ')
    #ip_addr = ip_addr.strip() - split already do this
    ip_octet_list = ip_addr.split('.')
    first_byte = int(ip_octet_list[0])
    if first_byte>0 and first_byte<=223:
        print(f'Type of IP {ip_addr} is - unicast ')
    elif first_byte>=224 and first_byte<=239:
        print(f'Type of IP {ip_addr} is - multicast ')
    elif ip_addr == '255.255.255.255':
        print(f'Type of IP {ip_addr} is - broadcast ')
    elif ip_addr == '0.0.0.0':
        print(f'Type of IP {ip_addr} is - unassigned ')
    else:
        print(f'Type of IP {ip_addr} is - unused ')


except ValueError:
    print('Please enter IP address (INT values, with dot as separator) in specified earlier format')