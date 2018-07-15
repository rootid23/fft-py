#Median of Two Sorted Arrays
#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#Find the median of the two sorted arrays. The overall run time complexity
#should be O(log (m+n)).
#Example 1:
#nums1 = [1, 3]
#nums2 = [2]
#The median is 2.0
#Example 2:
#nums1 = [1, 2]
#nums2 = [3, 4]
#The median is (2 + 3)/2 = 2.5

#4 qudrant search in remaing 2 quadrant
#O(log (m+n))
#Call 2 times getkth and k is about half of (m + n).
#Every time call getkth can reduce the scale k to its half. So the time complexity is log(m + n).

def findMedianSortedArrays(self, A, B):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    #A - xxxx  , B - xxxxxxxxxx
    def getkth(s,m,l,n,k) :
        if (m > n) :
            return getkth(l, n, s, m, k)
        if (m == 0) :
            return l[k - 1]
        if (k == 1) :
            return min(s[0], l[0])
        i,j = min(m, k / 2), min(n, k / 2)
        if (s[i - 1] > l[j - 1]) :
            return getkth(s, m, l[j:], n - j, k - j) #drop section 4
        else :
            return getkth(s[i:], m - i, l, n, k - i) #drop section 1
        return 0

    m,n = map(len, [A,B])
    l = (m + n + 1) >> 1;
    r = (m + n + 2) >> 1;
    return (getkth(A, m ,B, n, l) + getkth(A, m, B, n, r)) / 2.0




def findMedianSortedArrays(self, A, B):
    l = len(A) + len(B)
    if l % 2 == 1:
        return self.kth(A, B, l // 2)
    else:
        return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

def kth(self, a, b, k):
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2 , len(b) // 2
    ma, mb = a[ia], b[ib]

    # when k is bigger than the sum of a and b's median indices
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            return self.kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return self.kth(a[:ia], b, k)
        else:
            return self.kth(a, b[:ib], k)


#It's guaranteed to be O(log(min(m,n)) because every time the findKth function cuts the shorter array by half of its size.
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l=len(A)+len(B)
        return self.findKth(A,B,l//2) if l%2==1 else (self.findKth(A,B,l//2-1)+self.findKth(A,B,l//2))/2.0


    def findKth(self,A,B,k):
        if len(A)>len(B):
            A,B=B,A
        if not A:
            return B[k]
        if k==len(A)+len(B)-1:
            return max(A[-1],B[-1])
        i=len(A)//2
        j=k-i
        if A[i]>B[j]:
            #Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            return self.findKth(A[:i],B[j:],i)
        else:
            return self.findKth(A[i:],B[:j],j)





1:    double findMedianSortedArrays(int A[], int m, int B[], int n) {
2:      if((n+m)%2 ==0)
3:      {
4:        return (GetMedian(A,m,B,n, (m+n)/2) + GetMedian(A,m,B,n, (m+n)/2+1))/2.0;
5:      }
6:      else
7:        return GetMedian(A,m,B,n, (m+n)/2+1);
8:    }
9:       int GetMedian(int a[], int n, int b[], int m, int k)
10:       {
11:            assert(a && b);
12:            if (n <= 0) return b[k-1];
13:            if (m <= 0) return a[k-1];
14:            if (k <= 1) return min(a[0], b[0]);
15:            if (b[m/2] >= a[n/2])
16:            {
17:                 if ((n/2 + 1 + m/2) >= k)
18:                      return GetMedian(a, n, b, m/2, k);
19:                 else
20:                      return GetMedian(a + n/2 + 1, n - (n/2 + 1), b, m, k - (n/2 + 1));
21:            }
22:            else
23:            {
24:                 if ((m/2 + 1 + n/2) >= k)
25:                      return GetMedian( a, n/2,b, m, k);
26:                 else
27:                      return GetMedian( a, n, b + m/2 + 1, m - (m/2 + 1),k - (m/2 + 1));
28:            }
29:       }


def findMedianSortedArrays(self, A, B):
    l = len(A) + len(B)
    if l % 2 == 1:
        return self.kth(A, B, l // 2)
    else:
        return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

def kth(self, a, b, k):
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2 , len(b) // 2
    ma, mb = a[ia], b[ib]

    # when k is bigger than the sum of a and b's median indices
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            return self.kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return self.kth(a[:ia], b, k)
        else:
            return self.kth(a, b[:ib], k)




class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size(), len2 = nums2.size();
        int k = (len1 + len2 + 1) / 2; // for odd total it is the mid one, for even it is the left mid
        int num1 = findKth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, k);
        if ((len1 + len2) & 1) return num1;

        int num2 = findKth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, k + 1);
        return (num1 + num2) / 2.0;
    }

private:
    int findKth(vector<int>& nums1, int L1, int R1, vector<int>& nums2, int L2, int R2, int k) {
        if (L1 > R1) return nums2[L2 + k - 1];
        if (L2 > R2) return nums1[L1 + k - 1];
        int mid1 = L1 + (R1 - L1) / 2, mid2 = L2 + (R2 - L2);

        if (k <= (mid1 - L1) + (mid2 - L2) + 1) {
            if (nums1[mid1] <= nums2[mid2]) return findKth(nums1, L1, R1, nums2, L2, mid2 - 1, k);
            else return findKth(nums1, L1, mid1 - 1, nums2, L2, R2, k);
        } else {
            if (nums1[mid1] <= nums2[mid2]) return findKth(nums1, mid1 + 1, R1, nums2, L2, R2, k - (mid1 - L1) - 1);
            else return findKth(nums1, L1, R1, nums2, mid2 + 1, R2, k - (mid2 - L2) - 1);
        }
    }
};
