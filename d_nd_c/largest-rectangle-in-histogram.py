#84. Largest Rectangle in Histogram
#Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#The largest rectangle is shown in the shaded area, which has area = 10 unit.
#Example:
#Input: [2,1,5,6,2,3]
#Output: 10

  ## Divide and conquer w/ merge using expand technique
   def largestRectangleAreaDQ(A) :
     if (not A) :
       return 0
     return maxArea(A, 0, A.length - 1)

    def maxArea(A, l, r) :
        if (l == r)
            return A[l]
        m = l + (r - l) / 2
        area = maxArea(A, l, m)
        area = max(area, maxArea(A, m + 1, r))
        area = max(area, maxCombineArea(A, l, m, r))
        return area

    # Merge step
    def maxCombineArea(A, l, m, r) :
        i,j = m, m + 1 #Expand around mid
        area = 0
        h = min(A[i], A[j])
        while (i >= l && j <= r) :
            h = min(h, A[i], A[j])
            area = max(area, (j - i + 1) * h)
            if (i == l) :
                ++j
            elif (j == r) :
                --i
            else :
                if (A[i - 1] > A[j + 1])
                    --i
                else
                    ++j
        return area
