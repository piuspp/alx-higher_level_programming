#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if my_list[i] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i]):
    print(new_list)
