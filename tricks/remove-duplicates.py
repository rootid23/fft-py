
# For example, given nums = [0, 1, 1, 0, 3, 3, 0, 3, 4, 5, 0, 5, 5, 12], after calling your
#function, nums should be [1, 3, 4, 5, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0].

#Move idx in forward direction

def removeDuplicates(nums) :
  if(not nums) : return nums
  idx = 0
  prev = 0
  n = len(nums)
  for i in range(n) :
    if(nums[i] != 0 and prev != nums[i]) :
      nums[idx] = nums[i]
      prev = nums[idx]
      idx += 1
    else :
        nums[i] = 0
  for i in range(idx, n) :
    nums[i] = 0
  return nums

print ( removeDuplicates ( [ 0, 1, 1, 0, 3, 3, 0, 3, 4, 5, 0, 5, 5, 12] ) )

