# -*- coding: utf-8 -*-
# @Time    : 2020/6/24
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : bar.py
# @Software: PyCharm
# @Function: 

import numpy as np

def start_run():
    bar = [0, 0, 0]
    go = np.random.binomial(n=1, p=0.9)
    if go:
        position = np.random.randint(low=0, high=3)
        bar[position] = 1

    if bar[0] == 0 and bar[1] == 0:
        return True, bar[2]
    return False, 0


if __name__ == '__main__':
    repeat_times = 1000000

    meet_times = 0
    find_times = 0
    for i in range(repeat_times):
        meet, find = start_run()
        if meet == True:
            meet_times += 1
            find_times += find
    print(meet_times, find_times)
    print(find_times/meet_times)
