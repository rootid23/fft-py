#Given a non-empty array of integers, return the k most frequent elements.
#For example,
#Given [1,1,1,2,2,3] and k = 2, return [1,2].
#Note:
#You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
#Your algorithm's time complexity must be better than O(n log n), where n is
#the array's size.


class Solution():
  #1,1,1,2,2,3 -> k = 2 [1,2]
  #freque and number if (freq -> dynamic)
  #is it steaming?
  import heapq

  def topKFrequent(self, nums, k):
    frq_map = {}
    for i in range(len(nums)):
      if (nums[i] not in frq_map):
        frq_map[nums[i]] = 0
      frq_map[nums[i]] += 1
    pq = []
    for i, v in frq_map.iteritems():
      print i, v
      no = i
      frq = frq_map[i]
      heapq.heappush(pq, (frq, no))
      if (len(pq) > k):
        heapq.heappop(pq)
    rst = []
    while pq:
      rst.append(pq.pop()[1])
    return rst


from collections import Counter
import heapq


def topKFrequent(self, nums, k):
  c = Counter(nums)
  return heapq.nlargest(k, c, key=lambda x: c[x])
