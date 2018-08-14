
#https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.


def lcs(a, b) :
  m, n = map(len, [a, b])
  if(m == 0 or n == 0) : return 0
  if(a[0] == b[0]) :
    return 1 + lcs(a[1:], b[1:])
  return max(lcs(a, b[1:]), lcs(a[1:],b))

assert(lcs ("AAAA", "A") == 1)
assert(lcs ("ABCDGH", "ADH") == 3 )
assert(lcs ("AGGTAB", "GXTXAYB") == 4 )


