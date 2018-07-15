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

#eg. aba (expand with i,i from b) , baab  (expand with i,i+1 from a)

#We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded
#from its center, and there are only 2N-1 such centers.
#You might be asking why there are 2N-1 but not N centers? The reason is the center of a palindrome
#can be in between two letters. Such palindromes have even number of letters (such as “abba”) and its
center are between the two ‘b’s.
#2 types of palindormes even and odd with 2
#T - O(n^2)
def longestPalindrome(self, s):
    res = ""
    m = len(s)
    for i in range(s):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res

# get the longest palindrome, l, r are the middle indexes
# from inner to outer
def helper(self, s, l, r):
    m = len(s)
    while l >= 0 and r < m and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]


#longest palindorme substring
#Generate all substrings and get the maximum length substring
class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        def ispal(s) :
            return s == s[::-1]

        m = len(A)
        if(ispal(A)) : return A
        max_pal = ""
        for i in range(m) :
            for j in range(i+1, m+1) :
                nxtstr = A[i:j]
                # print(nxtstr)
                if(len(nxtstr) > len(max_pal) and ispal(nxtstr)) :
                    max_pal = nxtstr
        return max_pal

