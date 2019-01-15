
class Solution(object):
    def firstUniqChar(self, s):
        #find first character
        #use of set put in ordered
        #X sort - changs order
        # 2 pass -> how to avoid 2 pass
        mp = {}

        idx, rst = 0, len(s) + 1
        for c in s :
            if(c in mp) :
                mp[c] = -1
            else :
                mp[c] = idx

            idx += 1
        for k in mp.keys() :
            if(mp[k] != -1) :
                rst = min(mp[k], rst)

        return -1 if rst == len(s) + 1 else rst


#First Unique Character in a String
#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#Examples:
#s = "leetcode"
#return 0.
#s = "loveleetcode",
#return 2.
