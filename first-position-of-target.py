#First position of Target
#For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.
#If the target number does not exist in the array, return -1.
#Have you met this question in a real interview?
#Example
#If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.
#If the count of numbers is bigger than 2^32, can your code work properly?

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        #sorted, first index
        start = 0
        end = len(nums) - 1
        while start <= end :
            mid = start +  ( (end - start)//2 )
            #print(mid , start , end)
            if(nums[mid] == target) :
                if(mid > 0 and nums[mid] == nums[mid-1]) :
                    end -= 1
                else :
                    return mid
            elif(nums[mid] > target) :
                end = mid - 1
            else :
                start = mid + 1
        return -1
