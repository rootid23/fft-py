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


#Check pruning

#[] | start = 1
#  [1] | start = 2
#    [1, 2] | start = 3
#    [1, 3] | start = 4
#    [1, 4] | start = 5
#  [2] | start = 3
#    [2, 3] | start = 4
#    [2, 4] | start = 5
#  [3] | start = 4
#    [3, 4] | start = 5
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        #select 2 items from 1-4
        #[1,2,3,4] -> [1,2] [1,3] [1,4] [2,3] [2,4] [3,4]
        #n c K
        def csHelper(n, start, k, sel, ws = '\t') :
            print(ws + str(sel) + " | start = " +  str(start))
            rst = []
            #print(k, start)
            if(len(sel) == k) :
                rst += [ sel[:] ]
                return rst
            if(len(sel) > k) : return rst
            for idx in range(start, n) :
                remain = n - idx
                if(len(sel) + remain < k) : break # Pruning when we can't form elements
                sel += [ idx ]
                rst += csHelper(n, idx+1, k, sel, ws + '\t')
                sel.pop() #unchoose the decision  why [2,2]?

            return rst
        #
        return csHelper(n+1, 1, k, [])






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
