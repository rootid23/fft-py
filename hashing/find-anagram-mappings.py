
#O(N^2)
def anagramMappings(self, A, B):
  return [B.index(a) for a in A]

#O(N)
def anagramMappings(self, A, B):
  d = {b:i for i,b in enumerate(B)}
  return [d[a] for a in A]


class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        #A - [12, 28, ]
        #constraint -
        #is it sorted?
        #is it readonly?
        #how big is it can it fit in memonry?
        #duplicates?

        #Return indices in B

        #1. O(n^2) - look each element and get the index
        #2. O(N) + S - O(N) scan B once and store the <val,idx> in second scan for A return the result

        aux_map = {}
        rst = []
        for i,v in enumerate(B) :
            aux_map[v] = i

        for i,v in enumerate(A) :
            rst += [ aux_map[v] ]

        return rst

# Find Anagram Mappings
#Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.
#We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.
#These lists A and B may contain duplicates. If there are multiple answers, output any of them.
#For example, given
#A = [12, 28, 46, 32, 50]
#B = [50, 12, 32, 46, 28]
#We should return
#[1, 4, 3, 2, 0]
#as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4 because the 1st element of A appears at B[4], and so on.
#Note:
#A, B have equal lengths in range [1, 100].
#A[i], B[i] are integers in range [0, 10^5].
