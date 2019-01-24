
# Test case to think
# [2,0]
# 1
# [1]
# 1

#Case analysis
#w-f 1. [7,8,9,0,0,0], [2,5,6] 2. w-f [1,2,3,0,0,0], [4,5,6] 3. w-f [4,5,6,0,0,0], [5,6,7]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #Case analysis
        #w-f 1. [7,8,9,0,0,0], [2,5,6] 2. w-f [1,2,3,0,0,0], [4,5,6] 3. w-f [4,5,6,0,0,0], [5,6,7]
        last_idx = m + n - 1
        m, n = m - 1, n - 1
        while m >= 0 and n >= 0 :
            if(nums1[m] > nums2[n]) :
                nums1[last_idx] = nums1[m]
                m -= 1
            else :
                nums1[last_idx] = nums2[n]
                n -= 1
            last_idx -= 1

        while(last_idx >= 0 and n >= 0) :
            nums1[last_idx] = nums2[n]
            n -= 1
            last_idx -= 1

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        idx = m + n - 1
        m = m - 1
        n = n - 1
        while m >= 0 and n >= 0 :

            if(nums1[m] > nums2[n]) :
                nums1[idx] = nums1[m]
                m -= 1
            else :
                nums1[idx] = nums2[n]
                n -= 1
            idx -= 1

        while(n >= 0) :
            nums1[idx] = nums2[n]
            n -= 1
            idx -= 1

        #Use of slicing
        #if n > 0:
        #    nums1[:n] = nums2[:n]

#         if(n >= 0) :
#             for i in range(n, -1, -1) :
#                 nums1[i] = nums2[i]



#Merge Sorted Array
#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#Note:
#    The number of elements initialized in nums1 and nums2 are m and n respectively.
#    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
#Example:
#Input:
#nums1 = [1,2,3,0,0,0], m = 3
#nums2 = [2,5,6],       n = 3
#Output: [1,2,2,3,5,6]
