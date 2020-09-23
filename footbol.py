# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:22:41 2020

@author: Тонечка
"""
n = int(input())
dic = {}
for i in range(n):
    match = input().strip().split(';')
    if match[0] not in dic:
        dic[match[0]] = [0,0,0,0,0]
    if match[2] not in dic:
        dic[match[2]] = [0,0,0,0,0]
    dic[match[0]][0] += 1
    dic[match[2]][0] += 1
    if int(match[1]) > int(match[3]):
        dic[match[0]][4] += 3
        dic[match[0]][1] += 1
        dic[match[2]][3] += 1
    elif int(match[1]) < int(match[3]):
        dic[match[2]][4] += 3
        dic[match[2]][1] += 1
        dic[match[0]][3] += 1
    elif int(match[1]) == int(match[3]):
        dic[match[0]][4] += 1
        dic[match[0]][2] += 1
        dic[match[2]][4] += 1
        dic[match[2]][2] += 1

for key, value in dic.items():
    print(key+':',end = ' ')
    for j in value:
        print(j,end = ' ')
    print()
#for q, w in dic.items():
#    print((q+':'), *w, end='\n')

