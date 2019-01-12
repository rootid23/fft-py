
class Solution(object):


    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        dig, anti, col = set(), set(), set()

        def is_sol(r,c) :
            if(r+c in dig or r-c in anti or c in col) :
                return False
            return True

        def nowy(r, n) :
            cnt = 0
            if(r == n) :
                return 1
            for c in range(n) :
                if(is_sol(r,c) ) :
                    dig.add(r+c)
                    anti.add(r-c)
                    col.add(c)
                    cnt += nowy(r+1, n)
                    dig.remove(r+c)
                    anti.remove(r-c)
                    col.remove(c)
            return cnt



        #n number of queens
        return nowy(0, n)



#N-Queens II
#Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#Example:
#Input: 4
#Output: 2
#Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
#[
# [".Q..",  // Solution 1
#  "...Q",
#  "Q...",
#  "..Q."],
# ["..Q.",  // Solution 2
#  "Q...",
#  "...Q",
#  ".Q.."]
#]
