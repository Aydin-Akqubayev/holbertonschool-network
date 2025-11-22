#!/usr/bin/python3
def search_replace(my_list, elem_a, elem_b):
    res = []
    for i in my_list:
        if i == elem_a:
            res.append(elem_b)
        else:
            res.append(i)
    return res
