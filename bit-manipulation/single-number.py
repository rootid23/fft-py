class Solution(object):
    def singleNumber(self, nums):
        #appeared twice except 1
        #1. w/ set 2. w/ bit hacks XOR
        rst = nums[0]
        for idx in range(1, len(nums)) :
            rst = rst ^ nums[idx]
        return rst

        """
        :type nums: List[int]
        :rtype: int
        """


#Single Number
#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#Example 1:
#Input: [2,2,1]
#Output: 1
#Example 2:
#Input: [4,1,2,1,2]
#Output: 4
