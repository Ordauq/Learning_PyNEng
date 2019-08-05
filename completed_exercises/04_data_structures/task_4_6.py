# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

# Solution
ospf_block = ospf_route.split()
protocol = ospf_block[0]
prefix = ospf_block[1]
metric = ospf_block[2].strip('[]')
nh = ospf_block[4].strip(',')
last_upd = ospf_block[5].strip(',')
iface = ospf_block[6]
print(f"""
Protocol:           {protocol:>15}SPF
Prefix:                {prefix:>15}
AD/Metric:             {metric:>15}
Next-Hop:              {nh:>15}
Last Update:           {last_upd:>15}
Outbound Interface:    {iface:>15}""")



