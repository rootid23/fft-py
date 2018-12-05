#Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#Note: The solution set must not contain duplicate subsets.
#Example:
#Input: [1,2,2]
#Output:
#[
#  [2],
#  [1],
#  [1,2,2],
#  [2,2],
#  [1,2],
#  []
#]

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def subsetsWithDupHelper(nums, cs, k=0) :
            rst = []
            # if k == len(nums)  :
            rst += [ cs [:] ]
                # return rst
            for i in range(k, len(nums)) :
                if (i == k or nums[i-1] != nums[i]) :
                    cs += [ nums[i] ]
                    rst += subsetsWithDupHelper(nums, cs, i+1)
                    cs.pop()
            return rst


        nums.sort()
        return subsetsWithDupHelper(nums, [])
