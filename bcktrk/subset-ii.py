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

#Your input
#[4,4,4,1,4] -> [1,4,4,4,4]
#stdout
#	[] | start = 0
#		[1] | start = 1
#			[1, 4] | start = 2
#				[1, 4, 4] | start = 3
#					[1, 4, 4, 4] | start = 4
#						[1, 4, 4, 4, 4] | start = 5
#		[4] | start = 2
#			[4, 4] | start = 3
#				[4, 4, 4] | start = 4
#					[4, 4, 4, 4] | start = 5
#

class Solution(object):
    def subsetsWithDup(self, nums):

        nums.sort()

        def sDHelper(nums, start, sel, ws = '\t') :
            rst = []
            print(ws + str(sel) + " | start = " +  str(start))

            rst += [ sel [:] ] # add empty element
            for idx in range(start, len(nums)) :
                if(idx > start and nums[idx] == nums[idx - 1]) :
                    continue #Skip duplicates
                sel += [ nums [idx] ]
                rst += sDHelper(nums, idx+1, sel, ws + '\t')
                sel.pop()
            return rst

        return sDHelper(nums, 0, [])



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
