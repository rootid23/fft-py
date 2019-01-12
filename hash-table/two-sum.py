
class Solution(object):
    def twoSum(self, nums, target):
        #indices hasn;t changed
        #constraint

        #Is it sorted?
        #how to return - Is order matters
        #Idea - 1
        #1. all array w/ idx in aux map
        #2. and then scan + check if found any element
        #Idea - 2
        #1. store the remainder as go ahead

        a_map = {}
        for i, val in enumerate(nums) :
            if(val in a_map) :
                return [a_map[val], i]
            remainder = target - val
            a_map[remainder] = i
        return [-1,-1]


#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example:
#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
