#Can we use the given fact input ACGT

#Use 2 set w/ 1 Pass
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        keys = set()
        repeats = set()
        for i in range(len(s) - 9):
            substring = s[i : i + 10]

            if substring not in keys:
                keys.add(substring)
            else:
                repeats.add(substring)

        return list(repeats)

#Use of dictinary + 2 Pass
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT
        #AAAAACCCCC CCCCCAAAAA
        #How long?
        #In each iteration I'll get an array
        #BF - Store the last visited and if count > 1 put to the list
        #get the substring [0:10], [1:11], [2:12], [3:13]
        #XXA not the subsequence
        import collections
        a_map = collections.defaultdict(int)
        rst = []
        #In suffix [i:j] = [i, j)
        total_indxes = len(s) - 9
        for strt in range(total_indxes) :
            st = s[strt : strt+10]
            a_map[st] += 1
            strt += 1
        for k,v in a_map.items() :
            if(a_map[k] > 1) :
                rst += [k]
        return rst

#All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
#for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#Example:
#Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#Output: ["AAAAACCCCC", "CCCCCAAAAA"]
