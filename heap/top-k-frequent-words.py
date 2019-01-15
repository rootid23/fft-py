#Top K Frequent Words
#Given a non-empty list of words, return the k most frequent elements.
#Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word
#with the lower alphabetical order comes first.
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


#W/ custom sorting
import collections
import heapq
import functools

@functools.total_ordering
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = collections.Counter(words)

        freqs = []
        heapq.heapify(freqs)
        for word, count in counts.items():
            heapq.heappush(freqs, (Element(count, word), word))
            if len(freqs) > k:
                heapq.heappop(freqs)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(freqs)[1])
        return res[::-1]


# class Solution(object):
#     def topKFrequent(self, words, k):
#         """
#         :type words: List[str]
#         :type k: int
#         :rtype: List[str]
#         """
#         #Top k
#         #Top 10 from heap
#         #freq,
#         import heapq
#         import collections

#         mp = collections.defaultdict(int)
#         max_k, rst = [], []
#         for w in words :
#             mp[w] += 1

#         #generates the min heap
#         for key in mp.keys():
#             heapq.heappush(max_k, (mp[key], key) )
#             if(len(max_k) > k) :
#                 heapq.heappop(max_k)

#         #highest to lowest
#         #to break the tie with same count
#         while max_k :
#             rst += [ heapq.heappop(max_k)[1] ]

#         return rst



from collections import Counter
import heapq


class Solution(object):

  def topKFrequent(self, words, k):
    """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
    ## O(n log k)
    wMap = Counter(words)
    return heapq.nsmallest(k, wMap, key=lambda x: (-wMap[x], x))
    #Multi-dimensional sort with keeping the highest count (-ve) and smallest word x


## O(n log n) W/ custom sorting break ties w/ word
def topKFrequent(self, words, k):
    cntr = collections.Counter(words)
    candidates = cntr.keys()

    #sort w/ increasing order and break ties with string
    candidates.sort(key = lambda w: (-cntr[w], w))


    return candidates[:k]




import heapq
import collections


## O(n log n)
class Solution(object):

  def topKFrequent(self, words, k):
    count = collections.Counter(words)
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in xrange(k)]



