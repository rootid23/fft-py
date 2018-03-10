#!/usr/bin/env python
#Given an array of integers, find if the array contains any duplicates. Your function should return
#true if any value appears at least twice in the array, and it should return false if every element
#is distinct.


class Solution(object):

  #Cnstrnts
  #How many numbers will exists what is the limit?
  #Are they sorted?
  def containsDuplicate(self, nums):
    """
        :type nums: List[int]
        :rtype: bool
        """
    visited = set()
    for i in range(len(nums)):
      #print visited
      if (nums[i] in visited):
        return True
      visited.add(nums[i])

    return False


def containsDuplicate(self, nums):
  """
    :type nums: List[int]
    :rtype: bool
    """
  return len(nums) != len(set(nums))


# vim: ai ts=2 sts=2 et sw=2 tw=100 fdm=indent fdl=1
