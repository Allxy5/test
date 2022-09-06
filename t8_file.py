# -*- coding:utf-8 -*-
"""
作者: admin
日期: 2022年09月05日
"""
import os
import time
import zipfile

source=[r'G:\programming\python\file1']
target_dir=[r'G:\programming\python\file2']

target = target_dir[0] + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
#os.sep——根据所处平台，自动采取相应分隔符
#time.strftime——返回格式化时间

if not os.path.exists(target_dir[0]):
    os.mkdir(target_dir[0])

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
#压缩

print('zip command is')
print(zip_command)
print('Running')

# print(os.getcwd())
# q=['cd', os.getcwd(), '..']
# print(' '.join(q))
# os.system('cd ..')
# print(os.getcwd())


if os.system(zip_command) == 0:
    print('successful backup to', target)
else:
    print('backup failed')
