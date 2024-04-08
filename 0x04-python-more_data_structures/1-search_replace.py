#!/usr/bin/python3

def search_replace(my_list,search, replace):
    '''funtion that finds and
    replaces an element in a list'''
    new_list = []
    for i in range (0, len(my_list)):
        if my_list[i] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
    return (new_list)

