#Merge two given sorted integer array A and B into a new sorted integer array.
#Have you met this question in a real interview?
#Example
#A=[1,2,3,4]
#B=[2,4,5,6]
#return [1,2,2,3,4,4,5,6]
#Challenge
#How can you optimize your algorithm if one array is very large and the other is very small?


class Solution:
  """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

  def mergeSortedArray(self, A, B):
    # write your code here
    # A, B - Space?
    #L(A) == L(B) ?
    m, n = map(len, [A, B])
    rs = m + n
    C = [0] * rs
    # iterate over 2 arrays with i-> m,j ->n
    i = j = k = 0
    while i < m or j < n:
      if (i < m and j < n):
        if A[i] <= B[j]:
          C[k] = A[i]
          i += 1
        else:
          C[k] = B[j]
          j += 1
      else:
        if (i < m):
          C[k] = A[i]
          i += 1
        else:
          C[k] = B[j]
          j += 1
      k += 1
    return C
