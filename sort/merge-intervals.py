class Solution(object):
    def merge(self, intervals):
        #Case analysis
        #1.
        #---
        #  ----
        #2.
        #-----
        #  --
        #3.
        #-
        #  --
        m_i = []
        if(not intervals) : return m_i
        s_i = sorted(intervals, key=lambda item: item.start)
        m_i += [ s_i[0] ]
        for iv in range(1, len(s_i)) :
            if(m_i[-1].end >= s_i[iv].start) :
                m_i[-1].end = max(s_i[iv].end, m_i[-1].end)
            else :
                m_i += [ s_i[iv] ]
        return m_i

#Merge Intervals
#Given a collection of intervals, merge all overlapping intervals.
#Example 1:
#Input: [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#Example 2:
#Input: [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping.



