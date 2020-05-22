# -*- coding: utf-8 -*-
# @Time    : 2020/3/30
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : 01.py
# @Software: PyCharm
# @Function: 

import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))

if __name__ == '__main__':
    pass