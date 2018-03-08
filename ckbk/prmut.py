#!/usr/bin/env python

#Given a collection of distinct numbers, return all possible permutations.
#For example,
#[1,2,3] have the following permutations:
#[
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
#]


# Analysis OEIS
class Solution(object):

  def permute(self, nums):
    rst = []
    soFarList = []
    self.permuteHelper(nums, soFarList, rst)
    return rst

  def permuteHelper(self, nums, soFarList, rst):
    if (len(nums) == 0):
      rst.append(list(soFarList))

    for i in range(len(nums)):
      soFarList.append(nums[i])
      nxtChcLst = []
      rest = nums[0:i] + nums[i + 1:]  # of choices are reducing as we go down
      nxtChcLst.extend(rest)
      self.permuteHelper(nxtChcLst, soFarList, rst)
      soFarList.pop()


# W/ Library
def permute(self, nums):
  return list(itertools.permutations(nums))


# Use yield
def permute(self, nums):

  def gen(nums):
    n = len(nums)
    if n == 0:
      yield []
    else:
      for i in range(n):
        for cc in gen(nums[:i] + nums[i + 1:]):
          yield [nums[i]] + cc

  return list(gen(nums))


#Recursive, take any number as first
def permute(self, nums):
  return [[n] + p
          for i, n in enumerate(nums)
          for p in self.permute(nums[:i] + nums[i + 1:])] or [[]]


#Solution 2: Recursive, insert first number anywhere
#Insert the first number anywhere in any permutation of the remaining numbers.
def permute(self, nums):
  return nums and [
      p[:i] + [nums[0]] + p[i:]
      for p in self.permute(nums[1:])
      for i in range(len(nums))
  ] or [[]]


#Solution 3: Reduce, insert next number anywhere
#Use reduce to insert the next number anywhere in the already built
#permutations.
def permute(self, nums):
  return reduce(
      lambda P, n: [p[:i] + [n] + p[i:] for p in P for i in range(len(p) + 1)],
      nums, [[]])


# vim: ai ts=2 sts=2 et sw=2 tw=100 fdm=indent fdl=1
