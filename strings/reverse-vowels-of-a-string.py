#Reverse Vowels of a String
#Write a function that takes a string as input and reverse only the vowels of
#a string.
#Example 1:
#Given s = "hello", return "holle".
#Example 2:
#Given s = "leetcode", return "leotcede".

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowel = set( ['a', 'A', 'e', 'E','i', 'I','o', 'O','u', 'U'] )

        tmps = list(s)
        start = 0
        end = len(s) - 1
        while start < end:
            if(tmps[start] in vowel and tmps[end] in vowel)  :
                tmps[start], tmps[end] = tmps[end] , tmps[start]
                start += 1
                end -= 1
            if(tmps[start] not in vowel) :
                start += 1
            if(tmps[end] not in vowel) :
                end -= 1
        return "".join(tmps)
