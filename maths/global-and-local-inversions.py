
#All local inversions are global inversions.
#If the number of global inversions is equal to the number of local inversions,
#it means that all global inversions in permutations are local inversions.
#It also means that we can not find A[i] > A[j] with i+2<=j.
#In other words, max(A[i]) < A[i+2]
#
#In this first solution, I traverse A and keep the current biggest number cmax.
#Then I check the condition cmax < A[i+2]

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # i < j , A[i] > A[j]
        #[1, 0, 2]
        #Count the lacal === global iv
        #local === global
        #elements always from 0 -n -1
        m = len(A)

        #collect max as we go
        cmax  = A[0]
        for i in range(m - 2) :
            cmax = max(cmax, A[i])
            if(cmax > A[i+2]) :  #Current max always < A[i+2] or it will become global max
                return False
        return True

#Global and Local Inversions
#We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.
#The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].
#The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].
#Return true if and only if the number of global inversions is equal to the number of local
#inversions.
#Example 1:
#Input: A = [1,0,2]
#Output: true
#Explanation: There is 1 global inversion, and 1 local inversion.
#Example 2:
#Input: A = [1,2,0]
#Output: false
#Explanation: There are 2 global inversions, and 1 local inversion.
#Note:
#A will be a permutation of [0, 1, ..., A.length - 1].
#A will have length in range [1, 5000].
#The time limit for this problem has been reduced.
