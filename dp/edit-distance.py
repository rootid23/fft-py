#Edit Distance
#Given two words word1 and word2, find the minimum number of steps required to
#convert word1 to word2. (each operation is counted as 1 step.)
#You have the following 3 operations permitted on a word:
#a) Insert a character
#b) Delete a character
#c) Replace a character

# It works with suffix of both strings
# 3 sub problem


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
