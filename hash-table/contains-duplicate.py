

#cnstrnt : what it has O(n log N)?
#Ida
# 1. Sort
# 2. Auxillary set,  check if it contains element

#W/ auxillary set
class Solution(object):
    def containsDuplicate(self, nums):

        mp = set()
        for _,v in enumerate(nums) :
            if(v in mp) : return True
            mp.add(v)
        return False

#Contains Duplicate
#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#Example 1:
#Input: [1,2,3,1]
#Output: true
#Example 2:
#Input: [1,2,3,4]
#Output: false
#Example 3:
#Input: [1,1,1,3,3,4,3,2,4,2]
#Output: true
