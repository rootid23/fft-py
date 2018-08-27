#Given integers from 1-N present in the array of size N+1.
#Find the duplicate number
#i/p - lst = [1,2,3,4,4] o/p - 4

#!. Idea - Perform repeated binary and get the count and decide which directions to move
#If number of elements are less then mid then the duplicate element will be present in the 2nd half and vice versa.

def get_match_count(val, lst) :
    cnt = 0
    for v in lst:
        if(v == val) :
            cnt += 1
    return cnt

def get_lt_cnt(val, lst) :
    cnt = 0
    for v in lst :
        if(v < lst) :
            cnt += 1
    return cnt

def get_gt_cnt(val, lst) :
    cnt = 0
    for v in lst :
        if(v > lst) :
            cnt += 1
    return cnt

def detect_duplicate(a) :
    print(a)
    start, end = 1, len(a)

    while start < end :
        mid = start + (end - start)/2
        mid_cnt = get_match_count(a[mid], a)
        lt_cnt = get_lt_cnt(a[mid], a)
        gt_cnt = get_gt_cnt(a[mid], a)
        if(mid_cnt > 1) :
            return a[mid]
        if(lt_cnt > mid_cnt) :
            start = mid
        else :
            end = mid


lst = [3,3,3,1] #start = 1, end = 5 3< 0 = 3
#print(lst)
lst = [1,2,3,4,4]
print(detect_duplicate(lst))

