#Kth Largest Element in an Array
#Find the kth largest element in an unsorted array. Note that it is the kth
#largest element in the sorted order, not the kth distinct element.
#For example,
#Given [3,2,1,5,6,4] and k = 2, return 5.
#Note:
#You may assume k is always valid, 1 ≤ k ≤ array's length.


# O(n) time, quicksort-Partition method
def findKthLargest(self, nums, k):
  pos = self.partition(nums, 0, len(nums) - 1)
  if pos > len(nums) - k:
    return self.findKthLargest(nums[:pos], k - (len(nums) - pos)) #Include upto [0:pos)
  elif pos < len(nums) - k:
    return self.findKthLargest(nums[pos + 1:], k) #Include upto (pos+1:end]
  else:
    return nums[pos]


#https://www.geeksforgeeks.org/hoares-vs-lomuto-partition-scheme-quicksort/
# Lomuto partition scheme
def partition(self, nums, l, r):
  pivot = nums[r]
  lo = l
  for i in xrange(l, r):
    if nums[i] < pivot:
      nums[i], nums[lo] = nums[lo], nums[i]
      lo += 1
  nums[lo], nums[r] = nums[r], nums[lo]
  return lo


# O(n) time, quick selection
def findKthLargest(self, nums, k):
  # convert the kth largest to smallest
  return self.findKthSmallest(nums, len(nums) + 1 - k)


def findKthSmallest(self, nums, k):
  if nums:
    pvtIdx = self.partition(nums, 0, len(nums) - 1)
    if k > pvtIdx + 1:
      return self.findKthSmallest(nums[pvtIdx + 1:], k - pvtIdx - 1)
    elif k < pvtIdx + 1:
      return self.findKthSmallest(nums[:pvtIdx], k)
    else:
      return nums[pvtIdx]


# choose the right-most element as pivot
def partition(self, nums, l, r):
  idx = l
  while l < r:
    if nums[l] < nums[r]:  ## Tricky traversal like remove all 0s
      nums[l], nums[idx] = nums[idx], nums[l]
      idx += 1
    l += 1
  #pivot replacement
  nums[idx], nums[r] = nums[r], nums[idx]
  return idx


# O(nlgn) time
def findKthLargest1(self, nums, k):
  return sorted(nums, reverse=True)[k - 1]


def findKthLargest2(self, nums, k):
  nums.sort()
  return nums[-k]
  #l = len(nums)
  #return nums[l-k]


# k+(n-k)*log(k) time
def findKthLargest1(self, nums, k):
  heap = nums[:k]  # create array with k elements
  heapq.heapify(heap)  # create a max-heap whose size is k
  for num in nums[k:]:
    if num > heap[0]:
      heapq.heapreplace(heap, num)
    # or use:
    # heapq.heappushpop(heap, num)
  return heap[0]


# O(k+(n-k)lgk) time, min-heap
def findKthLargest3(self, nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)
  for _ in xrange(len(nums) - k):
    heapq.heappop(heap)
  return heapq.heappop(heap)
