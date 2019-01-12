
#Recursion
class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])

#swap w/ left and right
#python negative indexing
class SolutionClassicPythonic(object):
    def reverseString(self, s):
        s = list(s)
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]
        return ''.join(s)

class Solution(object):
    def reverseString(self, s):
        return s[::-1]

        """
        :type s: str
        :rtype: str
        """



#Reverse String
#Write a function that takes a string as input and returns the string reversed.
#Example 1:
#Input: "hello"
#Output: "olleh"
#Example 2:
#Input: "A man, a plan, a canal: Panama"
#Output: "amanaP :lanac a ,nalp a ,nam A"
