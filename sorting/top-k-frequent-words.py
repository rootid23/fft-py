
#Sorting collections.Counter
#W/ primary and secondary key

class Solution:
    def topKFrequent(self, words, k):
        counts = collections.Counter(words)
        items = list(counts.items())
        #Sort by the count and secondary by the word.
        #Note that by negating the count we sort from highest count to lowest
        #instead of the other way around. (Note also that you can't just do a reverse sort or the
        #words themselves would be the wrong way around.)
        items.sort(key=lambda item:(-item[1],item[0]))
        return [item[0] for item in items[0:k]]

#w/ Heap
import collections
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freqMap = collections.Counter(words)
        q = []
        for key in freqMap.keys() :
            heapq.heappush( q , (-freqMap[key], key) )
        rst = []
        for idx in range(0, k) :
            rst += [  heapq.heappop(q)[1] ]
        return rst

#w/ Heap Only 1 heapify operation
#heapify - transform list to heap
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in xrange(k)]


#Top K Frequent Words
#Given a non-empty list of words, return the k most frequent elements.
#Your answer should be sorted by frequency from highest to lowest. If two words have the same
frequency, then the word with the lower alphabetical order comes first.
#Example 1:
#Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
#Output: ["i", "love"]
#Explanation: "i" and "love" are the two most frequent words.
#    Note that "i" comes before "love" due to a lower alphabetical order.
#Example 2:
#Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
#Output: ["the", "is", "sunny", "day"]
#Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#    with the number of occurrence being 4, 3, 2 and 1 respectively.
#Note:
#    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
#    Input words contain only lowercase letters.
#Follow up:
#    Try to solve it in O(n log k) time and O(n) extra space.
