class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #a + b +c = 0
        #is it sorted?
        #duplicates in arrays? - yes
        #no duplicates

        #Idea
        #1. Sort
        #2. 2 pointer traversal
        #[-4,-1, -1, 0,1, 2]
        #.    i,j = A[i] + A[j] = -A[k]
        #How to fix duplicate triplet?

        m = len(nums)
        nums.sort()
        rst = []
        for k in range(m - 2) :
            a = -nums[k]
            #duplicate at start
            if(k > 0 and nums[k] == nums[k-1]) : continue
            l,r = k+1, m-1
            while(l < r) :
                b_plus_c = nums[l] + nums[r]
                if(a == b_plus_c) :
                    rst += [ [nums[k], nums[l], nums[r] ] ]
                    #Duplicates while picking the other 2 elements
                    l += 1
                    r -= 1
                    while(l < r and nums[l] == nums[l-1]) :
                        l += 1
                    while(l < r and nums[r] == nums[r+1]) :
                        r -= 1

                if(a > b_plus_c) : r -= 1
                if(a < b_plus_c) : l += 1
        return rst



#3Sum
#Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find
#all unique triplets in the array which gives the sum of zero.
#Note:
#The solution set must not contain duplicate triplets.
#Example:
#Given array nums = [-1, 0, 1, 2, -1, -4],
#A solution set is:
#[
#  [-1, 0, 1],
#  [-1, -1, 2]
#]
