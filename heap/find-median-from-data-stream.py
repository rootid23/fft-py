import heapq

class MedianFinder(object):
    #streaming numbers
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.small, num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        #heapq.heappush(self.large, -self.small[0])
        #heapq.heappop(self.small)
        #invariant - small > large - length
        #small(ascending) > large(desceding) - values
        if(len(self.small) < len(self.large)) :
            heapq.heappush(self.small, -heapq.heappop(self.large))
            #heapq.heappush(self.small, -self.large[0])
            #heapq.heappop(self.large)

    def findMedian(self):
        """
        :rtype: float
        """
        m, n = map(len, [self.small, self.large] )
        if(m == n) :
            return ( self.small[0] - self.large[0] ) / 2.0
        else :
            return float(self.small[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

#Find Median from Data Stream
#Median is the middle value in an ordered integer list. If the size of the
#list is even, there is no middle value. So the median is the mean of the two
#middle value.
#Examples:
#[2,3,4] , the median is 3
#[2,3], the median is (2 + 3) / 2 = 2.5
#Design a data structure that supports the following two operations:
#void addNum(int num) - Add a integer number from the data stream to the data
#structure.
#double findMedian() - Return the median of all elements so far.
#For example:
#addNum(1)
#addNum(2)
#findMedian() -> 1.5
#addNum(3)
#findMedian() -> 2
