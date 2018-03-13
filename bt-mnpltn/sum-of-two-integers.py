#!/usr/bin/env python

#Sum of Two Integers
#Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#Example:
#Given a = 1 and b = 2, return 3.

class Solution:

  # bit operation
  #it uses all bits to represnt the numbers
  def getSum(self, a, b):
    for _ in xrange(32):
      a, b = a ^ b, (a & b) << 1
      print(a, b)
    return a if a & 0x80000000 else a & 0xffffffff


# vim: ai ts=2 sts=2 et sw=2 tw=100 fdm=indent fdl=1
