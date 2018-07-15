#Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
#Example 1:
#Input:
#A: [1,2,3,2,1]
#B: [3,2,1,4,7]
#Output: 3
#Explanation:
#The repeated subarray with maximum length is [3, 2, 1].
#Note:
#    1 <= len(A), len(B) <= 1000
#    0 <= A[i], B[i] < 100

class Solution:

    def findLength(self, A, B):
        #subarray
        #bfs with maximum path
        #[1,1,1,1] [1,1,1,1,1]
        #Store the inxe as a litst

        #pick all substring and match (Bruteforce)

        m,n = map(len, [A, B])
        maxlen = 0
        store = set()
        for i in range(m) :
            for j in range(i, m) :
                store.add(tuple(A[i:j+1]))

        for i in range(n) :
            for j in range(i, n) :
                bsplit = tuple(B[i: j+1])
                if(bsplit in store) :
                    maxlen = max(maxlen, len(bsplit))

        return maxlen

#DP - NOTE - maximum length is not at end/start it is somewhere in the row
class Solution(object):
    def findLength(self, A, B):
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        return max(max(row) for row in dp)

