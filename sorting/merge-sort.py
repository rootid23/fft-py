

def merge_sort(a) :
    if(not a) : return a

    m = len(a)
    if(m > 1) :
        return merge(merge_sort(a[:m/2]), merge_sort(a[m/2:m]))
    else :
        return a

def merge(a, b) :
    m, n = map(len, [a, b])
    if(m == 0) : return b
    if(n == 0) : return a
    if(a[0] < b[0]) :
        return [ a[0] ] + merge(a[1:], b)
    else :
        return [ b[0] ]  + merge(a, b[1:])


assert merge_sort([10,2,5,3,7]) == sorted([10,2,5,3,7])
assert merge_sort([10,1]) == sorted([10,1])
assert merge_sort([10,1,-10]) == sorted([10,1,-10])

