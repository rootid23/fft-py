#Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#For example,
#If n = 4 and k = 2, a solution is:
#[
#  [2,4],
#  [3,4],
#  [2,3],
#  [1,2],
#  [1,3],
#  [1,4],
#]


# Iterative
def combine(self, n, k):
  ans = []
  stack = []
  x = 1
  while True:
    l = len(stack)
    if l == k:
      ans.append(stack[:])
    if l == k or x > n - k + l + 1:
      if not stack:
        return ans
      x = stack.pop() + 1
    else:
      stack.append(x)
      x += 1


#Combinations is typical application for backtracking.
#Two conditions for back track:
#(1) the stack length is already k
#(2) the current value is too large for the rest slots to fit in since we are using ascending order to make sure the uniqueness of each combination.
# Recursion
class Solution(object):

  def combine(self, n, k):
    """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
    rst = []

    def combHelper(n, k, tmp=[], r=1):  #r - remaining
      # print tmp, r
      if (len(tmp) > k):
        return
      if (len(tmp) == k):
        rst.append(list(tmp))
        #Choose
      for i in range(r, n + 1):
        tmp.append(i)
        #Explore
        combHelper(n, k, tmp, i + 1)
        #Unchoose
        tmp.pop()

    combHelper(n, k)
    return rst


#Recursion + Pruning
class Solution(object):

  def combine(self, n, k):
    """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
    res = []
    self.dfs(list(range(1, n + 1)), k, 0, res, [])
    return res

  def dfs(self, nums, k, index, res, path):
    if k == 0:
      res.append(path)
      return
    #Pruning if input is length
    if k > len(nums[index:]):
      return
    for i in xrange(index, len(nums)):
      self.dfs(nums, k - 1, i + 1, res, path + [nums[i]])
