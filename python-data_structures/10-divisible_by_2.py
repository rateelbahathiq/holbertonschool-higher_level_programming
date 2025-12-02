#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            value = True
            new_list.append(value)
        else:
            value = False
            new_list.append(value)
    return new_list
