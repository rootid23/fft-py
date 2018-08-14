


### Generate all substrings O(n^2)

#
for start in range(m) :
  for end in range(1, m-start+1) :
    print(astr[start: start+end])
