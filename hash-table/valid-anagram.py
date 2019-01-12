#Given two strings s and t , write a function to determine if t is an anagram of s.
#Example 1:
#Input: s = "anagram", t = "nagaram"
#Output: true
#Example 2:
#Input: s = "rat", t = "car"
#Output: false
#Note:
#You may assume the string contains only lowercase alphabets.
#Follow up:
#What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution(object):
    def isAnagram(self, s, t):

        #W/ aux_map
        import collections
        m,n = map(len , [s,t] )
        if(m != n) : return False
        mp = collections.defaultdict(int)
        for i in range(m) :
            mp[s[i]] += 1
            mp[t[i]] -= 1

        for k in mp.keys() :
            if(mp[k] != 0) : return False
        return True

        #String sorting
        return "".join(sorted(s)) == "".join(sorted(t))

