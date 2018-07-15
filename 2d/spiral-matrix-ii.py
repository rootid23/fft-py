#Given an integer n, generate a square matrix filled with elements from 1 to
#n2 in spiral order.
#For example,
#Given n = 3,
#You should return the following matrix:
#[
# [ 1, 2, 3 ],
# [ 8, 9, 4 ],
# [ 7, 6, 5 ]
#]

class Solution(object):

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rst = [ [0] * n ]
        for _ in range(n-1) :
            rst += [ [0] * n ]
        rStart, rEnd, cStart, cEnd,idx = 0,n-1,0,n-1,1
        while(rStart <= rEnd and cStart <= cEnd) :
            for i in range(cStart, cEnd+1) :
                rst[rStart][i] = idx
                idx += 1
            rStart += 1

            for i in range(rStart, rEnd+1) :
                rst[i][cEnd] = idx
                idx += 1
            cEnd -= 1

            if(rStart <= rEnd) :
                for i in range(cEnd, cStart-1, -1) :
                    rst[rEnd][i] = idx
                    idx += 1
            rEnd -= 1

            if(cStart <= cEnd) :
                 for i in range(rEnd, rStart-1, -1) :
                    rst[i][cStart] = idx
                    idx += 1
            cStart += 1

        return rst
