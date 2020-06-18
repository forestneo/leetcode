# -*- coding: utf-8 -*-
# @Time    : 2020/6/17
# @Author  : ForestNeo
# @Site    : forestneo.com
# @Email   : dr.forestneo@gmail.com
# @File    : chartst.py
# @Software: PyCharm
# @Function: 



import sys
input_str = "nhrwlbcc8m7c5hih9mhalw98k0322wf2jjm47kk3ntm9snfrflzzundn7d608usy049asxalzjk7izj6amcqhr8uubc04g52mcjboj2fmge2l6iarizfu4yve5o4i3srf5zgqbg82ckcotdeqp760mc9gzei5dzk5gj9x9yj05o3hle0ii64krkkp5i7blh7nbu3gu5vgi2scyn4yqx3z4vcjbyzhnqkh887izotjkg2l0mit0k14vyn39"
char = 't'
out = 0
input_str = input_str.lower()
for item in input_str:
    if item == char:
        out += 1
print(out)

if __name__ == '__main__':
    pass