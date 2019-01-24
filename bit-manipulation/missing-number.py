
class Solution(object):
    def missingNumber(self, nums):
        #priori info - [0,n]
        #[0,1,3]
        #BF - populate set with 0-n elem
        #pass 2 -> go over elements and remove the elemtn return not existing elem
        # 2 pass move the element to right position
        #[3,0,1] -> [0,1,2]

        #2 pass solution
         t = set()
         for i in range(len(nums)) :
             t.add(i)
         for i in range(len(nums)) :
             if(nums[i] in t) :
                 t.remove(nums[i])
         return t.pop() if len(t) > 0 else len(nums)

        #Bit manipulation w/ XOR
         missing_no = len(nums)
         for i, v in enumerate(nums) :
             missing_no ^= v ^ i
         return missing_no


#Missing Number
#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is
#missing from the array.
#Example 1:
#Input: [3,0,1]
#Output: 2
#Example 2:
#Input: [9,6,4,2,3,5,7,0,1]
#Output: 8
#Note:
#Your algorithm should run in linear runtime complexity. Could you implement it using only constant
#extra space complexity?
