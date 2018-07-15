#Unique Paths
#A robot is located at the top-left corner of a m x n grid (marked 'Start' in
#the diagram below).
#The robot can only move either down or right at any point in time. The robot
#is trying to reach the bottom-right corner of the grid (marked 'Finish' in
#the diagram below).
#How many possible unique paths are there?


class Solution(object):

  mem = {}

  # Top-down
  def uniquePaths(self, m, n):
    if (m < 1 or n < 1):
      return 0
    if (m == 1 and n == 1):
      return 1
    ky = str(m) + ":" + str(n)
    if (ky in self.mem):
      return self.mem[ky]
    self.mem[ky] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
    return self.mem[ky]

  # Recursion
  def uniquePaths(self, m, n):
    if (m < 1 or n < 1):
      return 0
    if (m == 1 and n == 1):
      return 1
    return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


#Recursion


class Solution:
  # @return an integer
  def uniquePaths(self, m, n):
    aux = [[1 for x in range(n)] for x in range(m)]
    for i in range(1, m):
      for j in range(1, n):
        aux[i][j] = aux[i][j - 1] + aux[i - 1][j]
    return aux[-1][-1]


# vim: ai ts=2 sts=2 et sw=2 tw=100 fdm=indent fdl=1
