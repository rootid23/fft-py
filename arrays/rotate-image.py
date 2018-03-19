class Solution(object):

  def rotate(self, matrix):
    """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
    end = len(matrix) / 2
    start = 0
    last = -1

    #swap hzntal elements
    while (start < end):
      matrix[start], matrix[last] = matrix[last], matrix[start]
      start += 1
      last -= 1

    #swap diagonal
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        if (i != j and i > j):
          matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


## List compression

  def rotate(self, A):
    A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]
