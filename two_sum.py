"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
def two_sum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    look_for = {}
    for ind, value in enumerate(nums):
        try:
            return look_for[value], ind
        except KeyError:
            # Key(remaining value to fulfill target) is not present in dict 
            # so add in dict
            look_for[target - value] = ind

arr = [2, 7, 1, 15]
target = 8
two_sum(arr, t)
