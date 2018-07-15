#Maximum Subarray
#Find the contiguous subarray within an array (containing at least one number)
#which has the largest sum.
#For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
#the contiguous subarray [4,-1,2,1] has the largest sum = 6


class Solution:
  # @param {integer[]} nums
  # @return {integer}
  def maxSubArrayHelper(self, nums, l, r):
    if l > r:
      return -sys.maxsize
    m = (l + r) / 2

    leftMax = sumNum = 0
    for i in range(m - 1, l - 1, -1):  #mid-1,l-1 -1
      sumNum += nums[i]
      leftMax = max(leftMax, sumNum)

    rightMax = sumNum = 0
    for i in range(m + 1, r + 1):  #mid+1->end
      sumNum += nums[i]
      rightMax = max(rightMax, sumNum)

    leftAns = self.maxSubArrayHelper(nums, l, m - 1)
    rightAns = self.maxSubArrayHelper(nums, m + 1, r)

    #left, right, ltmx+rtmx + nums[m]
    return max(leftMax + nums[m] + rightMax, max(leftAns, rightAns))

  def maxSubArray(self, nums):
    return self.maxSubArrayHelper(nums, 0, len(nums) - 1)
