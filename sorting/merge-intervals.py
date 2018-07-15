#return list of merge intervals
#cnstrnts
#1. how big interval list?
#2. max size int

#Ida1
#1. interval -> existing intervals-> update mark -visited - O(N^2)
#2. sort interval compare only end of previous w/ start of current and update interval
# O(n log n) + SC - O(k)


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if(len(intervals) < 1) : return intervals

        result = []

        #sorting
        intervals = sorted(intervals, key=lambda item: item.start)

        result.append(intervals[0])

        for i in range(1, len(intervals)) :
            if (result[-1].end >= intervals[i].start) :
                result[-1].end = max(result[-1].end, intervals[i].end)
                result[-1].start = min(result[-1].start, intervals[i].start)
            else :
                result.append(intervals[i])

        return result


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

#Given a collection of intervals, merge all overlapping intervals.
#Example 1:
#Input: [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#Example 2:
#Input: [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

