#!/usr/bin/python3

def common_elements(set_1, set_2):
    '''Function that returns common elements in two set'''
    c_set = []
    for item in set_1:
        for item2 in set_2:
            if item == item2:
                c_set.append(item)
    return(c_set)            

