#Given a list of numbers, return all possible permutations.
#Notice
#You can assume that there is no duplicate numbers in the list.
#Example
#For nums = [1,2,3], the permutations are:
#[
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
#]
#
class Solution:
  """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

  def permute(self, nums):
    # write your code here
    #total numbers in the array?
    # will there be any duplicates?

    #1 -> 2,3
    rst = []

    def permuteHelper(rest, curr):
      # k - levels
      n = len(rest)
      if (n == 0):
        rst.append(list(curr))

      for i in range(0, len(rest)):
        curr.append(rest[i])  #pick ith Ele from
        permuteHelper(rest[0:i] + rest[i + 1:], curr)  # next lvl - shrunk done
        curr.pop()

    permuteHelper(nums, [])
    return rst


class Solution(object):

  def permute(self, nums):
    rst = []
    choosen = []
    self.permuteHelper(nums, choosen, rst)
    return rst

  def permuteHelper(self, avail, choosen, rst):
    if (len(avail) == 0):
      rst.append(list(choosen))

    for i in range(len(avail)):
      choosen.append(avail[i])
      nxtAvail = avail[0:i] + avail[i + 1:]  #
      self.permuteHelper(nxtAvail, choosen, rst)
      choosen.pop()
