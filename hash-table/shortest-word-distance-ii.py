

class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.mp = {}
        for idx, word in enumerate(words) :
            if(word not in self.mp) :
                self.mp[word] = []
            self.mp[word] += [idx]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1 = self.mp[word1]
        w2 = self.mp[word2]
        min_diff = abs(min(w1) - max(w2))
        i, j = 0,0
        while i < len(w1) and j < len(w2) :
            min_diff = min(min_diff, abs(w1[i] - w2[j]))
            if(w1[i] < w2[j]) :
                i += 1
            else :
                j += 1
        return min_diff

        # for i in range(len(w1)) :
        #     v1 = w1[i]
        #     for j in range(len(w2)) :
        #         min_diff = min(min_diff, abs(v1 - w2[j]))
        # return min_diff




# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
#This is a follow up of Shortest Word Distance. The only difference is now you
#are given the list of words and your method will be called repeatedly many
#times with different parameters. How would you optimize it?
#Design a class which receives a list of words in the constructor, and
#implements a method that takes two words word1 and word2 and return the
#shortest distance between these two words in the list.
#For example,
#Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#Given word1 = "coding”, word2 = "practice”, return 3. Given word1 = "makes",
#word2 = "coding", return 1.
#Note
#You may assume that word1 does not equal to word2, and word1 and word2 are
#both in the list.
