
#Case analysis
# There're 3 possibilities to satisfy one edit distance apart:
# 1) Replace 1 char:
#  s: a B c
#  t: a D c
# 2) Delete 1 char from s:
#  s: a x b c
#  t: a    b c
# 3) Delete 1 char from t
#  s: a   b c
#  t: a x b c


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        #["practice", "makes", "perfect", "coding", "makes"]
        #coding, practice = 3
        #makes , coding = 1
        #constraint?
        #is word1, word2 equal?
        #w-f - word1/ word2 not present?
        #makes (1,4) , coding (3,5,9)
        #traverse update the dist and keep track of min

        #makes = 4, coding = 3
        #sd = 2
        d1, d2, sd = -1, -1, len(words)
        for idx, word in enumerate(words) :
            if(word == word1) :
                d1 = idx
            if(word == word2) :
                d2 = idx
            if(d1 != -1 and d2 != -1) :
                sd = min(sd, abs(d1 - d2))
        return sd

        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
#Shortest Word Distance
#Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#Example:
#Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#Input: word1 = “coding”, word2 = “practice”
#Output: 3
#Input: word1 = "makes", word2 = "coding"
#Output: 1
