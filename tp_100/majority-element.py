# -*- coding: utf-8 -*-

import unittest

#Given an array of size n, find the majority element. The majority element is
#the element that appears more than ⌊ n/2 ⌋ times.  You may assume that the
#array is non-empty and the majority element always exist in the array.

#cnstrnt :
#1. array is nonempty
#2. all ints
#3. exists majority elem
#Ida :
# 1. Travrse elem and maintain cnter
# 1,1,3,1 >
class Solution(object):

  def majorityElement(self, nums):
    count = 0
    candidate = None

    for num in nums:
      if count == 0:
        candidate = num
        count += (1 if num == candidate else -1)

    return candidate

  def majorityElement(self, nums):
    count = 0
    candidate = None

    for num in nums:
      if count == 0:
        candidate = num
        count += (1 if num == candidate else -1)

    return candidate

def test_answer():
  sol = Solution()
  assert majorityElement([1,3,5,5,5,5]) == 5

