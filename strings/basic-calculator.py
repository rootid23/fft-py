
#Basic Calculator
#Implement a basic calculator to evaluate a simple expression string.
#The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
#Example 1:
#Input: "1 + 1"
#Output: 2
#Example 2:
#Input: " 2-1 + 2 "
#Output: 3
#Example 3:
#Input: "(1+(4+5+2)-3)+(6+8)"
#Output: 23
#Note:
#    You may assume that the given expression is always valid.
#    Do not use the eval built-in library function.

#3 solution -  1. infx -> pstfx , 2. reverse the stirng 3. infx with sign store

## It handles "1 - (-1) - (-1)"

class Solution(object):
    def calculate(self, s):
        res, num, sign, stack = 0, 0, 1, [1]
        for i in s+"+": #<<<< modification
            if i.isdigit():
                num = 10*num + int(i)
            elif i in "+-":
                res += num * sign * stack[-1]
                sign = 1 if i=="+" else -1
                num = 0
            elif i == "(":
                stack.append(sign * stack[-1])
                sign = 1
            elif i == ")":
                res += num * sign * stack[-1]
                num = 0
                stack.pop()
        return res
