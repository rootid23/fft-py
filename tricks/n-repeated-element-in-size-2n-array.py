
def repeatedNTimes(self, A):
  for i in range(2, len(A)) :
    if(A[i] == A[i-1] or A[i] == A[i-2]) :
      return A[i]
    return A[0]


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #Pigenhole pronciple
        #2N -> N+1
        #[1,2,3,3] -> 2N = N, (N)
        #If element repeated 2N times
        #If find first recurring lement
        cnt, st = 0, set()

        for i in range(len(A)) :
            if(A[i] in st) :
                return A[i]
            st.add(A[i])
        return -1



#N-Repeated Element in Size 2N Array
#In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
#Return the element repeated N times.
#Example 1:
#Input: [1,2,3,3]
#Output: 3
#Example 2:
#Input: [2,1,2,5,3,2]
#Output: 2
#Example 3:
#Input: [5,1,5,2,5,3,5,4]
#Output: 5
#Note:
#4 <= A.length <= 10000
#0 <= A[i] < 10000
#A.length is even
