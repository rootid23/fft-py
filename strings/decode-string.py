#Given an encoded string, return it's decoded string.
#The encoding rule is: k[encoded_string], where the encoded_string inside the
#square brackets is being repeated exactly k times. Note that k is guaranteed
#to be a positive integer.
#You may assume that the input string is always valid; No extra white spaces,
#square brackets are well-formed, etc.
#Furthermore, you may assume that the original data does not contain any
#digits and that digits are only for those repeat numbers, k. For example,
#there won't be input like 3a or 2[4].
#Examples:
#s = "3[a]2[bc]", return "aaabcbc".
#s = "3[a2[c]]", return "accaccacc".
#s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

#Iterative
class Solution(object):
    def decodeString(self, s):
        #\d+[\w+]
        digit_stk = []
        char_stk = []

        char_str = ""
        num = 0
        idx = 0
        while idx < len(s) :
            if(s[idx] == '[') :  #leading number

                digit_stk += [ num ]
                char_stk += [ char_str ]
                #Reset
                num = 0
                char_str = ""
            elif(s[idx] == ']') : #ending parenthes
                times = digit_stk.pop()
                last_str = char_stk.pop()
                for _ in range(times) :
                    last_str += char_str
                char_str = last_str #char_str always contains result as it ends in valid parentheis
            elif(s[idx].isdigit()) :
                num = num * 10 + int(s[idx])
            else :
                char_str += s[idx]
            idx += 1

        return char_str

#Recursive
def helper(s):
    res = ""
    while s:
        num = ""
        while s and s[-1] in '0123456789':
            num += s.pop()
        if num:
            num = int(num)
            s.pop()
            res += helper(s) * num
        else:
            c = s.pop()
            if c not in "[]":
                res += c
            if c == ']':
                break
    return res

class Solution(object):
    def decodeString(self, s):
        return helper(list(s)[::-1])


