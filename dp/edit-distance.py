#Edit Distance
#Given two words word1 and word2, find the minimum number of steps required to
#convert word1 to word2. (each operation is counted as 1 step.)
#You have the following 3 operations permitted on a word:
#a) Insert a character
#b) Delete a character
#c) Replace a character

# It works with suffix of both strings
# 3 sub problem

#Recursion
def minDistance(self, word1, word2):
  #subproblmes
  m, n = map(len, [word1, word2])

  if(m == 0 or n == 0) : return m + n

  if(word1[-1] == word2[-1]) :
      return  self.minDistance(word1[0:m-1], word2[0:n-1])
  else :
      return min(self.minDistance(word1[0:m-1], word2),
                 self.minDistance(word1, word2[0:n-1]),
                 self.minDistance(word1[0:m-1], word2[0:n-1]))  + 1


#Reursion w/ memo dict
def minDistance(self, word1, word2, memo={}):
  m, n = map(len, [word1, word2])
  if (m == 0 or n == 0):
    return m + n
  if (word1, word2) in memo:
    return memo[word1, word2]
  memo[word1, word2] = min(
      self.minDistance(word1[1:], word2[1:], memo) +
      (1 if word1[0] != word2[0] else 0),
      self.minDistance(word1[1:], word2, memo) + 1,
      self.minDistance(word1, word2[1:], memo) + 1)
  return memo[word1, word2]

#Iteration w/ indexing
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #subproblem
        def minDistHelper(word1, word2, idxDict={}) :
            m, n = map(len, [word1, word2])
            # print( " ( m = %d, n = %d)" %(m,n) )

            if(m == 0 or n == 0) : return m + n
            cost = 0
            if( (m,n) in idxDict ) : return idxDict[ (m,n) ]
            if(word1[-1] == word2[-1]) :
                cost = minDistHelper(word1[0:m-1], word2[0:n-1], idxDict)
            else :
                cost = min(minDistHelper(word1[0:m-1], word2, idxDict),
                           minDistHelper(word1, word2[0:n-1], idxDict),
                        minDistHelper(word1[0:m-1], word2[0:n-1], idxDict))  + 1
            idxDict[ (m,n) ] = cost
            return idxDict[ (m,n) ]

        return minDistHelper (word1, word2)


#Iteration w/ array
class Solution(object):

  def minDistance(self, word1, word2):
    m, n = map(len, [word1, word2])
    if (m == 0 or n == 0):
      return m + n

    # 2-d intialization - tricky got from right to left
    opt = [range(n + 1)] + [[i] + [0] * n for i in xrange(1, m + 1)]

    #opt = [ [ 0 for _ in range(n+1)] for _ in range (m+1)]
    #for j in range(n+1) :
    #    opt[0][j] = j

    for i in range(1, m + 1):
      opt[i][0] = i
      for j in range(1, n + 1):
        opt[i][j] = min(opt[i - 1][j] + 1, opt[i][j - 1] + 1,
                        opt[i - 1][j - 1] +
                        (1 if word1[i - 1] != word2[j - 1] else 0))
    return opt[m][n]
