#Longest Palindromic Substring
#Given a string s, find the longest palindromic substring in s. You may assume
#that the maximum length of s is 1000.
#Example:
#Input: "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.
#Example:
#Input: "cbbd"
#Output: "bb"

class Solution:

    def longestPalindrome(self, s):
        #contrst -
        # 1. how long ? what char -set?
        #daaadb, aa (i, i+1) - for even
        #daba -> aba (i, i) - for odd

        def expand(start, end) :
            m = len(s)
            while(start >= 0 and end < m and s[start] == s[end]) :
                start -= 1
                end += 1
            return (s[start+1: end])

        if s == s[::-1] : return s

        m = len(s)

        maxstr = s[0]
        for i in range(m-1) :
            # odd case, like "aba"
            e = expand(i,i)
            # even case, like "abba"
            o = expand(i, i+1)
            el, ol, ml = map(len, [e, o, maxstr])
            if(el > max(ol, ml)) :
                maxstr = e
            if(ol > max(el, ml)) :
                maxstr = o

        return maxstr

