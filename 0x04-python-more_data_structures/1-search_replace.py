#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqueSet = set()
    for element in my_list:
        uniqueSet.add(element)
    result = sum(uniqueSet)
    return (result)
