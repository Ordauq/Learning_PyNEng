# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

# Solution
subnet = input('Please enter subnet in x.x.x.x/x format: ')
subnet_addr_str, subnet_mask_str = subnet.split('/')
subnet_mask = int(subnet_mask_str)
subnet_addr = subnet_addr_str.split('.')
ip_oct1, ip_oct2, ip_oct3, ip_oct4 = int(subnet_addr[0]), int(subnet_addr[1]), int(subnet_addr[2]), int(subnet_addr[3])

bin_mask = subnet_mask/8
print(bin_mask)
print(f"""
Network:
{subnet_addr[0]:<8} {subnet_addr[1]:<8} {subnet_addr[2]:<8} {subnet_addr[3]:<8}
{ip_oct1:>08b} {ip_oct2:>08b} {ip_oct3:>08b} {ip_oct4:>08b} 

Mask:
/{subnet_mask}

""")