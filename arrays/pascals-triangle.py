#Pascal's Triangle
#Given numRows, generate the first numRows of Pascal's triangle.
#For example, given numRows = 5,
#Return
#[
#     [1],
#    [1,1],
#   [1,2,1],
#  [1,3,3,1],
# [1,4,6,4,1]
#]


# T[i][j] = T[i-1][j-1] + T[i-1][j] iff i>1
#Faster 35ms
class Solution(object):

  def generate(self, numRows):
    """
        :type numRows: int
        :rtype: List[List[int]]
        """
    rst = []
    if (numRows == 0):
      return rst
    rst.append([1])
    strtIdx = 0
    while numRows > strtIdx + 1:
      crow = [1]
      for j in range(1, len(rst[strtIdx])):
        crow.append(rst[strtIdx][j - 1] + rst[strtIdx][j])
      crow.append(1)
      rst.append(crow)
      strtIdx += 1
    return rst


# T[i][j] = T[i-1][j-1] + T[i-1][j] iff i>1

  def generate(self, num_rows):
    triangle = []

    for row_num in range(num_rows):
      # The first and last row elements are always 1.
      row = [None for _ in range(row_num + 1)]
      row[0], row[-1] = 1, 1  #append 1

      # Each triangle element is equal to the sum of the elements
      # above-and-to-the-left and above-and-to-the-right.
      for j in range(1, len(row) - 1):
        row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

      triangle.append(row)

    return triangle
