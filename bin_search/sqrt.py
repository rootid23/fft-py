#Implement int sqrt(int x).
#Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#Example 1:
#Input: 4
#Output: 2
#Example 2:
#Input: 8
#Output: 2
#Explanation: The square root of 8 is 2.82842..., and since
#             the decimal part is truncated, 2 is returned.


#Template 1
#No duplicate input
#Initial Condition: left = 0, right = length-1
#Invariant: left <= right
#Termination: left > right
#Searching Left: right = mid-1
#Searching Right: left = mid+1

class Solution(object):

    #4 - 2 [1,2]
    #8 - 2 [1-4]
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        start = 0
        end = x // 2
        end += 1

        while start <= end :
            mid = start + (end - start)//2
            rst = mid * mid
            if(rst == x) : return mid
            elif(rst < x) : start = mid + 1
            else :
                end = mid - 1
        return start - 1

#         while start <= end :
#             rst = start * start
#             if(rst == x) : return start
#             if(rst > x) :
#                 return start - 1
#             start += 1
#         return start - 1

