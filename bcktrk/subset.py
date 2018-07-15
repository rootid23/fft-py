#Given a set of distinct integers, nums, return all possible subsets (the power set).
#Note: The solution set must not contain duplicate subsets.
#Example:
#Input: nums = [1,2,3]
#Output:
#[
#  [3],
#  [1],
#  [2],
#  [1,2,3],
#  [1,3],
#  [2,3],
#  [1,2],
#  []
#]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def subsetsHelper(rest, cur) :
            rst = []
            print(rest , cur)
            if(len(rest) == 0) :
                rst += [ cur[:] ]
                return rst
            cur += [ rest[0] ]
            rst += subsetsHelper(rest[1:], cur)
            cur.pop()
            rst += subsetsHelper(rest[1:], cur)
            return rst
        cur = []
        rst = subsetsHelper(nums, cur)
        return rst
