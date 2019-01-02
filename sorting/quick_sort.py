
def quicksort(nums, prf=""):
  print(prf + str(nums))
  if(not nums) :
    return nums
  #When we select the pivot it's always at the correct position
  pivot = nums[0]
  lesser = [num for num in nums if num < pivot]
  pivots = [num for num in nums if num == pivot]
  greater = [num for num in nums if num > pivot]
  return quicksort(lesser, prf + "\t") + pivots + quicksort(greater, prf + "\t")

print( quicksort([4,5,3,1]) )
