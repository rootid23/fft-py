#Move Zeroes
#Given an array nums, write a function to move all 0's to the end of it while
#maintaining the relative order of the non-zero elements.
#For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
#should be [1, 3, 12, 0, 0].
#Note:
#You must do this in-place without making a copy of the array.
#Minimize the total number of operations.


# TC : O(n)
class Solution(object):

  #Iteration with trick
  def moveZeroes(self, nums):
    strt = 0
    for i in range(len(nums)):
      if (nums[i] != 0): #It moves all zeros to end and reverse condition move them to front
        nums[i], nums[strt] = nums[strt], nums[i]
        strt += 1

  #W/ exception
  def moveZeroesWithXcept(self, nums):
    c = 0
    while True:
      try:
        nums.remove(0)
        c += 1
      except:
        nums += [0] * c
        break

