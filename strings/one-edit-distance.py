
class Solution(object):
    def isOneEditDistance(self, s, t):
        #s,t ->
        #3 cases
            #1. replace
            #2. delete from s (suffix of s from i + 1 == suffix of t )
            #3. insert into s i.e. delete from t  (suffix of s from i == suffix of t from i + 1 )
        m, n = map(len, [s, t])
        #Exact one edit distance is constraint
        if(s == t) : return False

        if(abs(m-n) > 1) : return False

        for i in range(min (m,n)) :
            if(s[i] != t[i]) : #mismatch
                if(s[i+1:] == t[i+1:] or s[i+1:] == t[i:] or s[i:] == t[i+1:] ) :
                    return True
                else :
                    return False
        return True

        #Is indxing location matters?
        #storing map w/ frequency will not work
        #Get the count of matching
        #Xor charcters -> cannot consider the idexes
        # 1. Nothing left 2. 1. element left -> what about duplicate characters
        #[a, b] [a, c, b]
        #count mismatch

#One Edit Distance
#Given two strings s and t, determine if they are both one edit distance apart.
#Note:
#There are 3 possiblities to satisify one edit distance apart:
#Insert a character into s to get t
#Delete a character from s to get t
#Replace a character of s to get t
#Example 1:
#Input: s = "ab", t = "acb"
#Output: true
#Explanation: We can insert 'c' into s to get t.
#Example 2:
#Input: s = "cab", t = "ad"
#Output: false
#Explanation: We cannot get t from s by only one step.
#Example 3:
#Input: s = "1203", t = "1213"
#Output: true
#Explanation: We can replace '0' with '1' to get t.
