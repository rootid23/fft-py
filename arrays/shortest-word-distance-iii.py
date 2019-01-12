
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #w-f words are same
        #keep track of list or deque
        import collections
        #[makes, ---- , makes]
        #handle word1 and word 2 differenlty
        #[0 | 1]
        sdq = collections.deque([])
        d1, d2, sd = -1,-1, len(words)
        for idx, word in enumerate(words) :
            if(word1 != word2) :
                if(word1 == word) :
                    d1 = idx
                if(word2 == word) :
                    d2 = idx
                if(d1 != -1 and d2 != -1) :
                    sd = min(sd, abs(d1 - d2))
            else :
                if(word1 == word) :
                    sdq += [ idx ]
                if(len(sdq) == 2) :
                    sd = min(sd, sdq[-1] - sdq[0])
                    sdq.popleft()

        return sd


#W/o deque
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #w-f words are same
        #keep track of list or deque

        #[makes, ---- , makes]
        #handle word1 and word 2 differenlty
        #[0 | 1]
        d1, d2, sd = -1,-1, len(words)
        for idx, word in enumerate(words) :
            if(word1 != word2) :
                if(word1 == word) :
                    d1 = idx
                if(word2 == word) :
                    d2 = idx

            else :
                if(word1 == word and d2 != -1) :
                    d1 = d2
                    d2 = idx
                if(word1 == word and d2 == -1) :
                    d2 = idx

            if(d1 != -1 and d2 != -1) :
                sd = min(sd, abs(d1 - d2))
        return sd







#Shortest Word Distance III
#Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#word1 and word2 may be the same and they represent two individual words in the list.
#Example:
#Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#Input: word1 = “makes”, word2 = “coding”
#Output: 1
#Input: word1 = "makes", word2 = "makes"
#Output: 3
#Note:
#You may assume word1 and word2 are both in the list.
