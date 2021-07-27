# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 06:18:02 2021

@author: acer
"""
from random import randrange
def qsort(lst):
    """
    Returns sorted list of integers with time complexity of O(nlogn)
    
    Input: list of integers 
    
    Output: Sorted list
    
    >>>qsort([12, 1, 2, 13, 21, 34, 55, 5, 19, 0, 200, 11])
    [0, 1, 2, 5, 11, 12, 13, 19, 21, 34, 55, 200]
    """
    if len(lst)<2:
        return lst 
    else:
        pivot = lst.pop(randrange(len(lst)))
        small = [elem for elem in lst if elem <= pivot]
        big = [elem for elem in lst if elem > pivot]
        return qsort(small) + [pivot]  + qsort(big)

test = qsort([12, 1, 2, 13, 21, 34, 55, 5, 19, 0, 200, 11])
print(test)

