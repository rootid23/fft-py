
#W/ 2 pointers
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rst = []
        m = len(nums)
        i = 0
        while i < m :
            start, end = i, i
            while(end+1 < m and  nums[end+1] - nums[end] == 1) :
                end += 1
            if(end > start) :
                rst += [ str(nums[start]) + "->" + str(nums[end]) ]
            else :
                rst += [ str(nums[start] ) ]
            i = end + 1

        return rst

#Summary Ranges
#Given a sorted integer array without duplicates, return the summary of its ranges.
#Example 1:
#Input:  [0,1,2,4,5,7]
#Output: ["0->2","4->5","7"]
#Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
#Example 2:
#Input:  [0,2,3,4,6,8,9]
#Output: ["0","2->4","6","8->9"]
#Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
