#Maximum Gap
#Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#Try to solve it in linear time/space.
#Return 0 if the array contains less than 2 elements.
#You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.


class Solution:

  def maximumGap(self, num):
    if len(num) < 2:
      return 0
    imin = min(num)
    imax = max(num)
    if (imin == imax):
      return 0
    gap = int(math.ceil(float(imax - imin) / (len(num) - 1)))
    # actually needed bucket numbers, reduce useless bucket
    bucketNum = int(math.ceil(float(imax - imin) / gap))
    bucketMin = [imax + 1] * bucketNum
    bucketMax = [imin - 1] * bucketNum
    for i in num:
      if i == imin or i == imax:
        continue
      idx = (i - imin) / gap
      bucketMin[idx] = min(bucketMin[idx], i)
      bucketMax[idx] = max(bucketMax[idx], i)
    maxgap = 0
    # consider min
    previous = imin
    for i in range(bucketNum):
      if bucketMin[i] == imax + 1 and bucketMax[i] == imin - 1:
        #empty bucket
        continue
      maxgap = max(maxgap, bucketMin[i] - previous)
      previous = bucketMax[i]
    #consider max
    maxgap = max(maxgap, imax - previous)
    return maxgap
