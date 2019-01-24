class Solution(object):
    def intersection(self, nums1, nums2):
        #2 arrays ?
        #sorted ?
        #size ?
        #fit in memory?
        #w/ set and hashmap
        m, n = map(len, [nums1, nums2])
        visited, dup = set(nums1), set()

        for i in range(n) :
            if(nums2[i] in visited) :
                dup.add(nums2[i])
        return list(dup)

    #w/ sorting
    def intersection(self, nums1, nums2):
        m, n = map(len, [nums1, nums2])
        nums1.sort()
        nums2.sort()
        dup = []
        i,j = 0, 0
        while i < m and j < n :
            if(nums1[i] < nums2[j]) :
                i += 1
            elif(nums1[i] > nums2[j]) :
                j += 1
            else :
                if(not dup or dup[-1] != nums1[i]) :
                    dup += [ nums1[i] ]
                i += 1
                j += 1
        return dup


#Intersection of Two Arrays
#Given two arrays, write a function to compute their intersection.
#Example 1:
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2]
#Example 2:
#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [9,4]
#Note:
#    Each element in the result must be unique.
#    The result can be in any order.
