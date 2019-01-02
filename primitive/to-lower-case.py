
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        A = ord('A')
        Z = ord('Z')
        a = ord('a')
        return "".join([(chr(ord(s) - A + a) if (A <= ord(s) <= Z) else s) for s in str])

#To Lower Case
#Implement function ToLowerCase() that has a string parameter str, and returns the same string in
#lowercase.
#Example 1:
#Input: "Hello"
#Output: "hello"
#Example 2:
#Input: "here"
#Output: "here"
#Example 3:
#Input: "LOVELY"
#Output: "lovely"
