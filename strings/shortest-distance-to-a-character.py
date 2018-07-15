#Scan Twice approach O(n)
def shortestToChar(self, S, C):
    n = len(S)

    #Init with res
    res = [n] * n
    #pos starts with -n
    pos = -n

    #Go back and forth between ranges
    #scan L-R - range(n)
    #Scan R-L - range(n)[::-1]:
    for i in range(n) + range(n)[::-1]:
        if S[i] == C:
          pos = i #
        res[i] = min(res[i], abs(i - pos)) # update the result
    return res


#Another idea is quite similar.
#We give it one more loop at first to find all character C and initialize distance to 0.
#The same, we can merge the extra pass to the forward pass one, like:
def shortestToChar(self, S, C):
       n = len(S)
       res = [0 if c == C else n for c in S]
       for i in range(n - 1): res[i + 1] = min(res[i + 1], res[i] + 1)
       for i in range(n - 1)[::-1]: res[i] = min(res[i], res[i + 1] + 1)
       return res

#Scan twice approach - O(N^2)
import collections

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        frnt = []
        m = len(S)
        rst = [0] * m
        for i in range(m):
            if(C != S[i]) :
                rst[i] = m
            else :
                frnt.append(i)

        for i in frnt: # This loop creates O(n^2)
            #go left and right
            lt, rt, dist = i-1, i+1, 1
            while(lt >= 0) :
                rst[lt] = min(dist, rst[lt])
                lt -= 1
                dist += 1
            dist = 1
            while(rt < m) :
                rst[rt] = min(dist, rst[rt])
                rt += 1
                dist += 1

        return rst

#Shortest Distance to a Character
#Given a string S and a character C, return an array of integers representing the shortest distance
#from the character C in the string.
#Example 1:
#Input: S = "loveleetcode", C = 'e'
#Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#Note:
#    S string length is in [1, 10000].
#    C is a single character, and guaranteed to be in string S.
#    All letters in S and C are lowercase.
