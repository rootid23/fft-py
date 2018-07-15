#Diff between wildcard matching is the * meaning -> match last occurances

#Recursion
class Solution(object):
    def isMatch(self, s, p):
        sLen, pLen = map(len, [s, p])

        if(pLen == 0) : return sLen == 0

        if (pLen > 1 and '*' == p[1]) :
            return self.isMatch(s, p[2:]) \
                   or sLen > 0 and (s[0] == p[0] or '.' == p[0]) \ #'matched 'last char/'any'
                   and self.isMatch(s[1:], p)  #abba, "ab*a"
        else :
            return sLen > 0 \
                and (s[0] == p[0] or '.' == p[0]) \
                and self.isMatch(s[1:], p[1:]) #starts with 'matched current char'/'any'

#W/ 2d array
def isMatch(self, s, p):
    m = len(s)
    n = len(p) #pattern len

    dp = [[True] + [False] * m]  #(m+1 cols + 1 row)

    for i in range(n): #n rows
        dp.append([False]*(m+1))

    for i in range(1, n + 1): #Iterate over pattern/rows
        x = p[i-1]
        if x == '*' and i > 1:
            dp[i][0] = dp[i-2][0]
        for j in range(1, m+1): #iterate over cols
            if x == '*':
                dp[i][j] = dp[i-2][j] or dp[i-1][j] or (dp[i-1][j-1] and p[i-2] == s[j-1]) or (dp[i][j-1] and p[i-2]=='.')
            elif x == '.' or x == s[j-1]:
                dp[i][j] = dp[i-1][j-1] #diagonal

    return dp[n][m]

#More pythonic
class Solution(object):
    def isMatch(self, s, p, memo={("",""):True}):
        if not p and s:      return False
        if not s and p:      return set(p[1::2]) == {"*"} and not (len(p) % 2)
        if (s,p) in memo:    return memo[s,p]

        char, exp, prev = s[-1], p[-1], 0 if len(p) < 2 else p[-2]
        memo[s,p] =\
               (exp == '*' and ((prev in {char, '.'} and self.isMatch(s[:-1], p, memo)) or self.isMatch(s, p[:-2], memo)))\
               or\
               (exp in {char, '.'} and self.isMatch(s[:-1], p[:-1], memo))
        return memo[s,p]

#Recursion
class Solution(object):
    def isMatch(self, text, pattern):

        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

#DP top down
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


#Bottom up
class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]

#Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#'.' Matches any single character.
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).
#Note:
#    s could be empty and contains only lowercase letters a-z.
#    p could be empty and contains only lowercase letters a-z, and characters like . or *.
#Example 1:
#Input:
#s = "aa"
#p = "a"
#Output: false
#Explanation: "a" does not match the entire string "aa".
#Example 2:
#Input:
#s = "aa"
#p = "a*"
#Output: true
#Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
#Example 3:
#Input:
#s = "ab"
#p = ".*"
#Output: true
#Explanation: ".*" means "zero or more (*) of any character (.)".
#Example 4:
#Input:
#s = "aab"
#p = "c*a*b"
#Output: true
#Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
#Example 5:
#Input:
#s = "mississippi"
#p = "mis*is*p*."
#Output: false
