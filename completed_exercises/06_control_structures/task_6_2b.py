# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

# Solution 
counter = 0
while(counter !=4):
    ip_addr = input('Hello. Please enter IP address in format x.x.x.x: ')
    #ip_addr = ip_addr.strip() - split already do this
    ip_octet_list = ip_addr.split('.')
    validated_ip = []
    if len(ip_octet_list) == 4:
        for octet in ip_octet_list:
            int_oct = int(octet)
            if int_oct >=0 and int_oct<=255:
                validated_ip.append(int_oct)
                counter+=1
            else:
                print('Неправильный IP-адрес')
                break

    else:
        print('Неправильный IP-адрес')


if len(validated_ip) == 4:
    first_byte = int(validated_ip[0])
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
