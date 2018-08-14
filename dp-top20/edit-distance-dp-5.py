
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.


# Input:   str1 = "geek", str2 = "gesek"
# Output:  1
# We can convert str1 into str2 by inserting a 's'.

# Input:   str1 = "cat", str2 = "cut"
# Output:  1
# We can convert str1 into str2 by replacing 'a' with 'u'.

# Input:   str1 = "sunday", str2 = "saturday"
# Output:  3
# Last three and first characters are same.  We basically
# need to convert "un" to "atur".  This can be done using
# below three operations.
# Replace 'n' with 'r', insert t, insert a

def edit_distance(a, b) :
  m, n = map(len, [a, b])
  if(m == 0) : return n
  if(n == 0) : return m
  if(a[0] == b[0]) :

    return edit_distance(a[1:], b[1:])
  #3 cases 1. insert 2. delete 3. replace
  return 1 + min(edit_distance(a, b[1:]), edit_distance(a[1:],b), edit_distance(a[1:], b[1:]))

# print(edit_distance ("cat", "cut"))
assert(edit_distance ("geek", "gesek") == 1)
assert(edit_distance ("cat", "cut") == 1 )
assert(edit_distance ("sunday", "saturday") == 3 )

