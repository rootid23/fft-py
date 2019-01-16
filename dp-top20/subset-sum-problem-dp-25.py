
#Measure the time w/ time python dp-top20/subset-sum-problem-dp-25.py
# Subset Sum Problem | DP-25

# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given
#set with sum equal to given sum.

# Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output:  True  //There is a subset (4, 5) with sum 9.

#Include last element or not

def subset_sum(a, total) :
  m = len(a)
  if(m == 0) : return False
  if(total == 0) : return True
  val = a[m-1]
  return subset_sum(a[:m-1],total - val) or subset_sum(a[:m-1],total)

def subset_sum_dp(a, total) :
  m = len(a)
  if(total < 0) : return False
  if(m == 0) : return False
  if(total == 0 or total == a[m-1]) : return True
  val = a[m-1]
  return subset_sum(a[:m-1],total - val) or subset_sum(a[:m-1],total)

# print(edit_distance ("cat", "cut"))
#assert(subset_sum([3, 34, 4, 12, 5, 2], 9) == True)
assert(subset_sum_dp([3, 34, 4, 12, 5, 2], 9) == True)

