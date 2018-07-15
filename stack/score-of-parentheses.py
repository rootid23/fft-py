#Given a balanced parentheses string S, compute the score of the string based on the following rule:
#    () has score 1
#    AB has score A + B, where A and B are balanced parentheses strings.
#    (A) has score 2 * A, where A is a balanced parentheses string.
#
#Example 1:
#Input: "()"
#Output: 1
#Example 2:
#Input: "(())"
#Output: 2
#Example 3:
#Input: "()()"
#Output: 2
#Example 4:
#Input: "(()(()))"
#Output: 6
#
#Note:
#    S is a balanced parentheses string, containing only ( and ).
#    2 <= S.length <= 50

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        # 1. When ) found and only 1 ( present
        # 2. when ) found and more than 1 (
        stk = []
        for c in S :
            if(c == '(') :
                stk += [-1]
            else :
                cur = 0
                while (stk[-1] != -1):
                    cur += stk.pop()
                stk.pop()
                stk += [ 1 if cur == 0 else cur * 2]
        total = 0
        while stk :
            total += stk.pop()
        return total
