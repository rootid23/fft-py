#Total # of subsequences O(2^n) = # of subsets

def getSubsequence(st, k, lst) :
  if(k == len(st)) :
    print(lst)

  for i in range(k, len(st)) :
    #pick the character
    lst += [ st[k] ]
    getSubsequence(st, i+1, lst)
    lst.pop()

st = 'abcd'
k = 0
lst = []
getSubsequence(st, k, lst)
