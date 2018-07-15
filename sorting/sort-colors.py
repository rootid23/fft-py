#Sort Colors
#Given an array with n objects colored red, white or blue, sort them so that
#objects of the same color are adjacent, with the colors in the order red,
#white and blue.
#Here, we will use the integers 0, 1, and 2 to represent the color red, white,
#and blue respectively.
#Note:
#You are not suppose to use the library's sort function for this problem.

#3 pointers lt,rt,idx
class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #[2,0,2,1,1,0] -> [0, 1 ,2]

        #1. count total and write - O(n)
        # OR
        #2. [,       ,2]
        # OR partion find kth smallest element
        #3 colors
        #0,2,1
        #lt - 0
        lt,rt,idx = 0, len(nums)-1, 0
        while idx <= rt :
            if(nums[idx] == 0) : #Move 0 to start
                nums[idx],nums[lt] = nums[lt],nums[idx]
                idx += 1
                lt += 1
            elif(nums[idx] == 2) : #Move 2 to end
                nums[idx],nums[rt] = nums[rt],nums[idx]
                rt -= 1
            else :
                idx += 1 #move the pointer in case of 1


#NOTE : 1. idx and lt always move in forward direction
#2. rt always move in reverse direction
