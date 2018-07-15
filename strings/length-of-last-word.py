#Length of Last Word
#Given a string s consists of upper/lower-case alphabets and empty space
#characters ' ', return the length of last word in the string.
#If the last word does not exist, return 0.
#Note: A word is defined as a character sequence consists of non-space
#characters only.
#For example,
#Given s = "Hello World",
#return 5.

import re
class Solution:

    def lengthOfLastWord(self, s):
        #checks of empty string
        if not s :
            return 0
        #spliit the string with regex remove all empty spaces
        lst = re.split('\s+', s)

        m = len(lst[-1])

        return len(lst[-2]) if m == 0 else m
