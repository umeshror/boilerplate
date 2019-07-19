"""
You are given a list of n-1 integers and these integers are in the range of 1 to n. 
There are no duplicates in the list. One of the integers is missing in the list. 
Write an efficient code to find the missing integer.
"""

def getMissingNumber(arr): 
    n = len(arr) 
    total = (n + 1)*(n + 2)/2
    sum_of_arr = sum(arr) 
    return total - sum_of_arr
