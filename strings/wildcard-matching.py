class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = map(len, [s, p])

        #m+1 rows, n+1 cols
        f = [ [True] + [False] * n ]
        for i in range(m) :
            f.append([False] * (n+1))


        for i in range(1, n+1) :
            f[0][i] = p[i-1] == '*' and f[0][i-1]

        for i in range(1, m+1) :
            for j in range(1, n+1) :
                if(p[j-1] != '*') :
                    if(p[j-1] == '?' or s[i-1] == p[j-1]) :
                        f[i][j] = f[i-1][j-1]
                else :
                    f[i][j] = f[i][j-1] or f[i-1][j]

        return f[m][n]


#Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#'?' Matches any single character.
#'*' Matches any sequence of characters (including the empty sequence).
#The matching should cover the entire input string (not partial).
#Note:
#    s could be empty and contains only lowercase letters a-z.
#    p could be empty and contains only lowercase letters a-z, and characters like ? or *.
#Example 1:
#Input:
#s = "aa"
#p = "a"
#Output: false
#Explanation: "a" does not match the entire string "aa".
#Example 2:
#Input:
#s = "aa"
#p = "*"
#Output: true
#Explanation: '*' matches any sequence.
#Example 3:
#Input:
#s = "cb"
#p = "?a"
#Output: false
#Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
#Example 4:
#Input:
#s = "adceb"
#p = "*a*b"
#Output: true
#Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
#Example 5:
#Input:
#s = "acdcb"
#p = "a*c?b"
#Output: false
