


import collections

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        pal_len = 0
        is_odd_len = False
        frq_map = collections.Counter(s)
        for k in frq_map.keys() :
            if(frq_map[k] % 2 == 0) :  pal_len += frq_map[k]
            else :
                pal_len += frq_map[k] - 1
                is_odd_len = True
        return pal_len + 1 if is_odd_len == True else pal_len


#Count odds:
    def longestPalindrome(self, s):
        return len(s) - max(sum(v & 1 for v in collections.Counter(s).values()) - 1, 0)

#Count evens:
    def longestPalindrome(self, s):
        return min(sum(v & ~1 for v in collections.Counter(s).values()) + 1, len(s))

#I count how many letters appear an odd number of times.
#Because we can use all letters, except for each odd-count letter we must leave one, except one of them we can use.
#Python:
def longestPalindrome(self, s):
    odds = sum(v & 1 for v in collections.Counter(s).values())
    return len(s) - odds + bool(odds)

#Longest Palindrome
#Given a string which consists of lowercase or uppercase letters, find the
#length of the longest palindromes that can be built with those letters.
#This is case sensitive, for example "Aa" is not considered a palindrome here.
#Note:
#Assume the length of given string will not exceed 1,010.
#Example:
#Input:
#"abccccdd"
#Output:
#7
#Explanation:
#One longest palindrome that can be built is "dccaccd", whose length is 7.
