#Palindrome Partitioning
#Given a string s, partition s such that every substring of the partition is a palindrome.
#Return all possible palindrome partitioning of s.
#Example:
#Input: "aab"
#Output:
#[
#  ["aa","b"],
#  ["a","a","b"]
#]

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        #Check wheather "aab" | "a" -> expsfx("ab")
        #a a b
        #aa b
        #a a b
        #aaa
        def is_pal(st) :
            return st == st[::-1]
        #Select the prefix if palindrome and explore the suffix
        def partitionHelper(s, clst, tmp='\t') :
            rst = []
            #print( tmp + "avail = " + s + " | ch = " + str(clst))
            if(len(s) == 0) :
                #print(",".join(clst))
                rst += [ clst[:] ]
            for i in range(len(s)) :
                if is_pal(s[:i+1]) :
                    clst += [ s[:i+1] ]
                    rst += partitionHelper(s[i+1:], clst, tmp+ '\t')
                    clst.pop()
            return rst
        clst = []
        rst = partitionHelper(s, clst)
        return rst
