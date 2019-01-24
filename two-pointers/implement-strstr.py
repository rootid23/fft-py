#substring
#"hello" "ll" = (5,2)
#0.
#Case analysis
#1. w-f needle at mid  "hello" "ll" 2. at start "hello" "he" 3. at end "hello" "lo"
#Ida
#1. get the needle and scan over all haystack
m, n = map(len, [haystack, needle])
if(haystack == needle) : return 0
t_len = m - n + 1 # 1 is added due to python range is < not <=
for i in range(t_len) :
    start, end = i, i + n
    print(i)
    if(needle == haystack[start:end]) :
        return i
return -1

#Implement strStr().
#Returns the index of the first occurrence of needle in haystack, or -1 if
#needle is not part of haystack.
