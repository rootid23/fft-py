#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#Given two integers x and y, calculate the Hamming distance.
#Note:
#0 ≤ x, y < 231.
#Example:
#Input: x = 1, y = 4
#Output: 2
#Explanation:
#1   (0 0 0 1)
#4   (0 1 0 0)
#       ↑   ↑
#The above arrows point to positions where the corresponding bits are different.

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count("1")

#How numbers represented in python?
#How to handle -ve numbers?
def hamming_distance(x, y):
    xor = x ^ y
    d = 0
    while xor > 0:
        d += xor & 1
        xor >>= 1
    return d

#Can't handle negative numbers
#negative number throws the computer into an infinite loop
def hamming_distance(x, y):
  diff = x ^ y
  cnt = 0
  while(diff) :
      diff &= diff - 1 #clear the least significant bit set
      cnt += 1
  return cnt

#To overcome the limitation of negative numbers
def hamming_distance(x, y):
        diff = x ^ y
        cnt = 0
        for _ in range(32) :
            if(diff == 0) : break
            diff &= diff - 1 #clear the least significant bit set
            cnt += 1
        return cnt

        return bin(x^y).count('1') # bin operation
