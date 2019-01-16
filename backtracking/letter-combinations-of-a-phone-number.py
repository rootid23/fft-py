
class Solution(object):
    def lcHelper(self, digits, aux_lst, rst) :
        #base case do nothing
        lst = []
        if(len(digits) == 0) :
            lst += ["".join(rst)] if rst else []
            return lst
        options = aux_lst[ int(digits[0]) ]
        for c in options :
            rst += [c]
            lst +=  self.lcHelper(digits[1:], aux_lst, rst)
            rst.pop()
            #OR  lst +=  self.lcHelper(digits[1:], aux_lst, rst + [c])
        return lst


    def letterCombinations(self, digits):
        #"23" - >
        aux_lst = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        #       23
        #  a   b    c  -> k = 0
        #ab            -> 1
        #              -> 2
        return self.lcHelper(digits, aux_lst, [])


#Letter Combinations of a Phone Number
#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that
#the number could represent.
#A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does
#not map to any letters.
#Example:
#Input: "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#Note:
#Although the above answer is in lexicographical order, your answer could be in any order you want.
