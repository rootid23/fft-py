
#Keep indexes of good candidates in deque d. The indexes in d are from the current window, they're increasing,
#and their corresponding nums are decreasing. Then the first deque element is the index of the largest window value.
#Use indices

def maxSlidingWindow(self, nums, k):
    d = collections.deque()
    out = []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d += i,
        if d[0] == i - k: #eg.  [1,3,1,2,0,5] , 3
            d.popleft()
        if i >= k - 1:
            out += nums[d[0]],
    return out

# Use values
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        #What to store? next possible maximum
        #How to store?
        #Pick the mx values in linear time

        from collections import deque
        m = len(nums)
        mx_vals, ax_dq = [], deque()

        for i in range(m) :
            #Keep only maximum
            while(ax_dq and ax_dq[-1] < nums[i]) :
                ax_dq.pop()

            #Store maximum
            ax_dq += [ nums[i] ]

            if(i >= k-1) :
                mx_vals += [ ax_dq[0] ]
                #Go back k steps and compare if we retained the maxium in dq
                #eg.  [1,3,1,2,0,5] ,3
                if(nums[i - k + 1] == ax_dq[0]) :
                    print(ax_dq)
                    ax_dq.popleft()
        return mx_vals



#Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
#
#Example:
#
#Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
#Output: [3,3,5,5,6,7]
#Explanation:
#
#Window position                Max
#---------------               -----
#[1  3  -1] -3  5  3  6  7       3
# 1 [3  -1  -3] 5  3  6  7       3
# 1  3 [-1  -3  5] 3  6  7       5
# 1  3  -1 [-3  5  3] 6  7       5
# 1  3  -1  -3 [5  3  6] 7       6
# 1  3  -1  -3  5 [3  6  7]      7
#Note:
#You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.
#
#Follow up:
#Could you solve it in linear time?
