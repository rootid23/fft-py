#Diagonal Traverse
#Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal
order as shown in the below image.
#Example:
#Input:
#[
# [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
#]
#Output:  [1,2,4,7,5,3,6,8,9]
#Explanation:
#Note:
#    The total number of elements of the given matrix will not exceed 10,000.

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        r = []
        if(not matrix) : return r

        m,n = map(len, [matrix, matrix and matrix[0]])

        for d in range(m+n-1) : #0,1,2,3,4
            if(d%2 == 1) :
                #change direction
                for i in range(max(0, d-n+1), min(d+1,m)) :
                    r += [ matrix[i][d-i] ] #
            else :
                for i in range(max(0, d-m+1), min(d+1,n)) :
                    r += [ matrix[d-i][i] ] #
        return r


#Deque & Dictionary - O(MN)
#1. Property for the diagonals is that: row + col = constant. This constant varies from 0 to M+N-2.
#2. The direction of the diagonal is top to bottom or bottom to top. The direction depends if constant
#is even or odd.
#3.Iterate the matrix. Maintain a dictionary with key as integer and value as a deque.
#4.The key will be row+col and deque will have all elements which have the same row +col. Depending
#5. whether row+col is even or odd, we will either append or appendleft.
from collections import deque, defaultdict

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if (not matrix) :
            return []
        M, N = map(len, [matrix, matrix[0]])
        result = defaultdict(deque)
        max_sum = M+N-2
        for i in range(M):
            for j in range(N):
                s = i+j
                if s&1:
                    result[s].append(matrix[i][j])
                else:
                    result[s].appendleft(matrix[i][j])
        output = []
        for s in range(max_sum+1):
            output.extend(result[s])
        return output


#Within diagonal row+col is same, so we first sort index pairs by row+col, and within diagonal sort
#them either by row or by column index depending if row+col is odd/even.

def findDiagonalOrder(self, matrix):
    l = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))]
    l.sort(key=lambda x: sum(x) * 100000 - x[sum(x)%2])
    return [matrix[x][y] for x, y in l]


def findDiagonalOrder(self, matrix):
        l = [[i,j] for i in range(len(matrix)) for j in range(len(matrix[0]))]
        l.sort(key=lambda x: float(x[0]+x[1])-float(x[(x[0]+x[1])%2])*0.00000001 )
        return [matrix[x][y] for [x,y] in l]

#annotate the matrix entries with coordinate information so that we can just sort them by that.
def findDiagonalOrder(self, matrix):
    entries = [(i+j, (j, i)[(i^j)&1], val)
               for i, row in enumerate(matrix)
               for j, val in enumerate(row)]
    return [e[2] for e in sorted(entries)]

#just walk over the matrix in the desired order. My d is the diagonal number, i.e., i+j. So I can
#compute j as d-i.
def findDiagonalOrder(self, matrix):
    m, n = len(matrix), len(matrix and matrix[0])
    return [matrix[i][d-i]
            for d in range(m+n-1)
            for i in range(max(0, d-n+1), min(d+1, m))[::d%2*2-1]]


#Why the range range(max(0, d-n+1), min(d+1, m))? Well I need 0 <= i < m and 0 <= j < n. As said
#above, j is d-i, so I have 0 <= d-i < n. Isolating i gives me i <= d and i > d-n. Since we're
#dealing with integers, they're equivalent to i < d+1 and i >= d-n+1. So my i needs to be in the
#range [0, m) as well as in the range [d-n+1, d+1). And my range is simply the intersection of those
#two ranges.


#Simple two step approach:
#1- Group numbers according to diagonals. Sum of row+col in same diagonal is same.
#2- Reverse numbers in odd diagonals before adding numbers to result list.
#
 def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = [ ]
        dd = collections.defaultdict(list)
        if not matrix: return result
        # Step 1: Numbers are grouped by the diagonals.
        # Numbers in same diagonal have same value of row+col
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                dd[i+j+1].append(matrix[i][j]) # starting indices from 1, hence i+j+1.
        # Step 2: Place diagonals in the result list.
        # But remember to reverse numbers in odd diagonals.
        for k, v in dd.iteritems():
            if k%2==1: dd[k].reverse()
            result += dd[k]
        return result


for k, v in dd.iteritems():
    if k % 2 == 1:
        result += v[::-1]
    else:
        result += v
return result
