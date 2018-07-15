# Arranging Coins
#You have a total of n coins that you want to form in a staircase shape, where
#every k-th row must have exactly k coins.
#Given n, find the total number of full staircase rows that can be formed.
#n is a non-negative integer and fits within the range of a 32-bit signed
#integer.
#Example 1:
#n = 5
#The coins can form the following rows:
#¤
#¤ ¤
#¤ ¤
#Because the 3rd row is incomplete, we return 2.
#Example 2:
#n = 8
#The coins can form the following rows:
#¤
#¤ ¤
#¤ ¤ ¤
#¤ ¤
#Because the 4th row is incomplete, we return 3.
#[0,n]

class Solution:
    def arrangeCoins(self, n):
        #predicate : sum of 1 ~ mid > n
        def p(mid) :
            son = (mid * (mid + 1)) # 2
            return son > n

        while(start < end) :
            mid = start + (end - start + 1)#2
            if(p(mid)) : end = mid - 1
            else : start = mid
        return start

        #linear
        #1 - 1, 2- 2, 3 -3
        # coins = n
        # scase = 0
        # while n > 0 :
        #     scase += 1
        #     coins -= scase
        # return scase if coins == 0 else scase - 1
        start = 0
        end = n
