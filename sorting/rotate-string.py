#Rotate String
#Given a string and an offset, rotate string by offset. (rotate from left to right)
#Example
#Given "abcdefg".
#offset=0 => "abcdefg"
#offset=1 => "gabcdef"
#offset=2 => "fgabcde"
#offset=3 => "efgabcd"
#Challenge
#Rotate in-place with O(1) extra memory.

#Note : Simillar to pancake sorting
#1. Move to top
#1. Swap the items upto offset
#1. Swap the remaining elements from offset to keep other elements intact

class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, st, offset):
        # write your code here

        def swap(strt, end) :
            while strt < end :
                st[strt], st[end] = st[end], st[strt]
                strt += 1
                end -= 1

        n = len(st)
        #abcdefg -> gabcdef
        if(n > 0) :
            offset = offset % len(st)
            #Move to top
            swap(0, n - 1)
            #swap the items
            swap(0, offset-1)
            #swap the remaining to keep other elements intact
            swap(offset, n-1)


#Rotate Array
#Rotate an array of n elements to the right by k steps.
#For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to
#[5,6,7,1,2,3,4].

#Original List                   : 1 2 3 4 5 6 7
#After reversing all numbers     : 7 6 5 4 3 2 1
#After reversing first k numbers : 5 6 7 4 3 2 1
#After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

