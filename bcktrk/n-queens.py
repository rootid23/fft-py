
class Solution(object):
    def solveNQueens(self, n):
        q = [ ['.'] * n ]
        for _ in range(1, n) :
            q += [ ['.'] * n ]

        dig,anti,col = set(), set(),set()

        def is_safe(r,c) :
            if(r+c in dig or r-c in anti or c in col) :
                return False
            return True

        def solveNQueensHelper(n, r, q) :
            rst = []
            if(r == n) :
                rst += [[ "".join(x[:]) for x in q ]]
                return rst

            for c in range(n) :
                if(is_safe(r,c)) :
                        dig.add(r+c)
                        anti.add(r-c)
                        col.add(c)
                        q[r][c] = 'Q'
                        rst += solveNQueensHelper(n, r+1, q)
                        q[r][c] = '.'
                        dig.remove(r+c)
                        anti.remove(r-c)
                        col.remove(c)
            return rst

        r = 0
        return solveNQueensHelper(n, r, q)


#N-Queens
#The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#Given an integer n, return all distinct solutions to the n-queens puzzle.
#Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#Example:
#Input: 4
#Output: [
# [".Q..",  // Solution 1
#  "...Q",
#  "Q...",
#  "..Q."],
# ["..Q.",  // Solution 2
#  "Q...",
#  "...Q",
#  ".Q.."]
#]
