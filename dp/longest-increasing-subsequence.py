#Longest Increasing Subsequence
#Given an unsorted array of integers, find the length of longest increasing subsequence.
#Example:
#Input: [10,9,2,5,3,7,101,18]
#Output: 4
#Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
#Note:
#    There may be more than one LIS combination, it is only necessary for you to return the length.
#    Your algorithm should run in O(n2) complexity.
#Follow up: Could you improve it to O(n log n) time complexity?


class Solution(object):
    def lengthOfLIS(self, nums):

        #[10,9,2,5,3,7,101,18] 4
        #2,3,7,101

        # L(curr) = 1 + max( L(prev) ) where 0 < prev < curr and arr[curr] > arr[prev]; or
        # L(curr) = 1, if no such prev exists.
        #O(n^2)
        if(not nums) : return 0

        m = len(nums)
        L = [0] * m
        L[0], max_ans = 1, 1

        for curr in range(1, m) :
            mx = 0
            for prev in range(curr) : #Go from 0 to end
                if(nums[curr] > nums[prev]) :
                    mx = max(mx, L[prev])
            L[curr] = mx + 1
            max_ans = max(max_ans, L[curr]) #Look for the maximum element
        return max_ans


        #O(2^n)
         def lengthOfLISHelper(nums, idx, prev) :
             if(idx == len(nums)) :
                 return 0
             taken = 0
             if(nums[idx] > prev) :
                 taken = 1 + lengthOfLISHelper(nums, idx+1, nums[idx])

             not_taken = lengthOfLISHelper(nums, idx+1, prev) #not taken go with the last element
             return max(taken, not_taken)

         if(not nums) : return 0
         return lengthOfLISHelper(nums, 0, float('-inf'))

