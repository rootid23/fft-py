

class Solution(object):
    def diStringMatch(self, S):

        #S - 'I' , 'D' A[i] < A[i+1]
        #[0,1,2,3,4]
        # Total length = n-1 and # of set = O(N)
        # "IDID"-  [0,4,2,3,1] - []
        #          #n-1 compare result
                   #0,1,2,3,4
        #1. Naive way - generate all permutation and compate it w/ string if match return output
        #   O(2^n) + O(n) - scan
        #2. We can use pruning with given string?
        #   How to intelligenlty prune the result?
        #3. Think different? How to select the element to insert?
        #4. Greedy : Reverse the result when condition is not satisfied
        lt, rt = 0, len(S)
        rst = []
        #for c in S + S[-1]:
        for i in range(len(S)) :
            if S[i] == 'I' :
                rst.append(lt)
                lt += 1
            else :
                rst.append(rt)
                rt -= 1

        return rst + [lt]

        #greedy approach
         res = list(range(len(S) + 1))
         for i, s in enumerate(S):
             if s == 'I' and res[i] > res[i+1] or s == 'D' and res[i] < res[i+1]:
                 res[i:] = res[i:][::-1]
         return res

        """
        :type S: str
        :rtype: List[int]
        """



#DI String Match
#Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
#Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#If S[i] == "I", then A[i] < A[i+1]
#If S[i] == "D", then A[i] > A[i+1]
#Example 1:
#Input: "IDID"
#Output: [0,4,1,3,2]
#Example 2:
#Input: "III"
#Output: [0,1,2,3]
#Example 3:
#Input: "DDI"
#Output: [3,2,0,1]
#Note:
#1 <= S.length <= 10000
#S only contains characters "I" or "D".
