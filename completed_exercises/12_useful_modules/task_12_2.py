# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

'''

# Solution

def split_to_ip(single_network):
    ''' Accept as argument single network (example: 1.1.1.1-3 or 1.1.1.1-1.1.1.3)
        Working only for last octet :(
    '''
    ip_addr = []
    simple_octet = ''
    all_octet = []
    #for network in single_network:
    all_octet = single_network.split('.')

    for octet in all_octet:
        if '-' not in octet:
            simple_octet += (octet + '.')
        else:
            if len(all_octet) <= 4:
                first_part, last_part = octet.split('-')
                last_part = int(last_part) + 1
                for i in range (int(first_part), int(last_part)):
                    k = (simple_octet + str(i))
                    ip_addr.append(k)
            else:
                first_part, _ = octet.split('-')
                last_part = all_octet[-1]
                last_part = int(last_part) + 1
                for i in range (int(first_part), int(last_part)):
                    k = (simple_octet + str(i))
                    ip_addr.append(k)

    return ip_addr

networks = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

def convert_ranges_to_ip_list(networks):
    ip_addr_list = []
    for network in networks:
        if '-' not in network:
            ip_addr_list.append(network)
        else:
            result = split_to_ip(network)
            for entity in result:
                ip_addr_list.append(entity)
               

    return ip_addr_list

print(convert_ranges_to_ip_list(networks))
