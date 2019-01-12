
#Explode from right
def flipAndInvertImage(self, A):
    return [[1 ^ i for i in row[::-1]] for row in A]

#In place solution
#We can do this in place. In each row, the ith value from the left is equal to the inverse of the ith value from the right.
#We use (C+1) / 2 (with floor division) to iterate over all indexes i in the first half of the row, including the center.
class Solution(object):
    def flipAndInvertImage(self, A):
        for row in A:
            for i in xrange((len(row) + 1) / 2):
                """
                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                """
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for idx in range(len(A)) :
            A[idx] = A[idx][::-1]
            for j in range(len(A[idx])) :
                A[idx][j] = abs(A[idx][j] - 1)
        return A

#W/ lambda
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return map(lambda row: map(lambda x: 1 if x == 0 else 0, row[::-1]), A)

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # 1. m *n = > m *n
        # 2. read only
        m , n = map(len, [A, A[0]])

        for i in range (m) :
            lt, rt = 0, n-1
            while lt < rt :
                A[i][lt], A[i][rt] = A[i][rt], A[i][lt]
                lt += 1
                rt -= 1

        #Flip
        for i in range (m) :
            for j in range (n) :
                A[i][j] = 1 - A[i][j]
        return A

#W/ -ve indexing
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # 1. m *n = > m *n
        # 2. read only
        m , n = map(len, [A, A[0]])

        for i in range (m) :
            for j in range(n//2) :
                A[i][j], A[i][~j] = A[i][~j], A[i][j]

        #Flip
        for i in range (m) :
            for j in range (n) :
                A[i][j] = 1 - A[i][j]

        return A




#Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
#To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
#To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
#Example 1:
#Input: [[1,1,0],[1,0,1],[0,0,0]]
#Output: [[1,0,0],[0,1,0],[1,1,1]]
#Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
#Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
#Example 2:
#Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
#Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
#Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#Notes:
#    1 <= A.length = A[0].length <= 20
#    0 <= A[i][j] <= 1
