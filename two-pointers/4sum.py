class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        rst = []
        if(len(nums) < 4) : return rst
        #(a+b) = target - (c+d) #if c+d ^ then value @ rhs will drop
        #[-2, -1, 0, 0, 1, 2]
        m = len(nums)

        for i in range(m-3) :
            #skip duplicates during the first elem
            if(i > 0 and nums[i] == nums[i-1]) : continue
            for j in range(i+1, m-2) :
                 #skip duplicates during second ele
                if(j > i+1 and nums[j] == nums[j-1]) : continue
                sum_ = nums[i] + nums[j]

                l,r = j+1, m-1
                while(l < r) :
                    #skip duplicates during thrid and forth elemen
                    mtgt = target - (nums[l] + nums[r])
                    if(mtgt == sum_) :
                        rst += [ [nums[i], nums[j], nums[l], nums[r]] ]
                        l += 1
                        r -= 1
                        while(l < r and (nums[l] == nums[l-1])) : l += 1
                        while(l < r and (nums[r] == nums[r+1])) :  r -= 1

                    if(mtgt > sum_) :
                        l += 1
                    if(mtgt < sum_) :
                        r -= 1
        return rst

    #-1,0  = (0,2)

#4Sum
#Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
#such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of
#target.
#Note:
#The solution set must not contain duplicate quadruplets.
#Example:
#Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#A solution set is:
#[
#  [-1,  0, 0, 1],
#  [-2, -1, 1, 2],
#  [-2,  0, 0, 2]
#]
