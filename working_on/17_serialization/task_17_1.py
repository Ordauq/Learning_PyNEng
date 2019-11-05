# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv), в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''

# Solution

import glob
import re
import csv

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']

def parse_sh_version(line):
    IOS_REGEX = 'Cisco IOS Software, \S+ Software \S+ Version ([^,]+)'
    IMAGE_REGEX = 'System image file is \"(\S+:\S+)\"'
    UPTIME_REGEX = 'router uptime is (\d+ days, \d+ hours, \d+ minutes)'
    IOS = ''.join(re.findall(IOS_REGEX, line))
    IMAGE = ''.join(re.findall(IMAGE_REGEX, line))
    UPTIME = ''.join(re.findall(UPTIME_REGEX, line))
    result = (IOS, IMAGE, UPTIME)
    #print(result)
    return result

def file_to_line(filename):
    with open(filename, 'r') as SHOW_FILE:
        file_on_line = SHOW_FILE.read()
    
    return file_on_line

def write_inventory_to_csv(data_filenames, csv_filename):
    with open(csv_filename, 'w',) as file_results:
        writer = csv.writer(file_results, delimiter=';')
        writer.writerow(headers)
        for file in data_filenames:
            final_result = []
            DEVICE_NAME = re.match('sh_version_(\S+).txt', file)
            result = parse_sh_version(file_to_line(file))
            final_result.append(DEVICE_NAME.group(1))
            for i in result:
                final_result.append(i)
            #print(f)
            writer.writerow(final_result)

    return None

files = ['sh_version_r1.txt', 'sh_version_r2.txt', 'sh_version_r3.txt']


write_inventory_to_csv(files, 'routers_inventory.csv')
#for item in file_to_line(files):
#    print(item)





