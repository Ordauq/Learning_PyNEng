# -*- coding: utf-8 -*-
'''
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

# Solution
def generate_trunk_config(intf_vlan_mapping, trunk_template):
    '''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12': [10, 20, 30],
         'FastEthernet0/14': [11, 30],
         'FastEthernet0/16': [17]}
    trunk_template - список команд для порта в режиме trunk

    Возвращает список всех портов в режиме trunk с конфигурацией на основе шаблона
    '''
    result = {}
    for k,v in intf_vlan_mapping.items():
        result[f'interface {k}'.rstrip()] = []
        for entry in trunk_template:
            if entry.endswith('allowed vlan'):
                #result[f'interface {k}'.rstrip()] = f'{entry} {",".join(str(i) for i in v)}'.rstrip()
                result[f'interface {k}'.rstrip()].append(entry + ' ' + ",".join(str(i) for i in v).rstrip())
                #result.append(f'{entry} {",".join(str(i) for i in v)}'.rstrip())
            else:
                result[f'interface {k}'.rstrip()].append(entry.rstrip())
        
    return result

to_print = generate_trunk_config(trunk_config, trunk_mode_template)
print(to_print)