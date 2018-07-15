#You are a product manager and currently leading a team to develop a new
#product. Unfortunately, the latest version of your product fails the quality
#check. Since each version is developed based on the previous version, all the
#versions after a bad version are also bad.
#Suppose you have n versions [1, 2, ..., n] and you want to find out the first
#bad one, which causes all the following ones to be bad.
#You are given an API bool isBadVersion(version) which will return whether
#version is bad. Implement a function to find the first bad version. You
#should minimize the number of calls to the API.
#Credits:
#Forward declaration of isBadVersion API.

#Template 2
#Duplicate input and find first duplicate

#Initial Condition: left = 0, right = length
#Invariant left < right
#Searching Left: right = mid
#Searching Right: left = mid+1


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        #first duplicate
        while (start < end) :
            mid = start + (end - start)/2
            if(isBadVersion(mid)) :
                end = mid
            else :
                start = mid + 1
        return start

