#!/usr/bin/python3
def unique(unique):
    res = []
    for i in range(len(unique)):
        if unique[i] not in unique[:i]:
            res.append(unique[i])
    return res


def uniq_add(my_list):
    my_list = unique(my_list)
    sum = 0
    for i in my_list:
        sum += i
    return sum
