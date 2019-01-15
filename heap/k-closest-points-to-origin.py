#
class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]

class Solution(object):
    def kClosest(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def work(i, j, K):
            if i >= j: return
            oi, oj = i, j
            pivot = dist(random.randint(i, j))
            while i < j:
                while i < j and dist(i) < pivot: i += 1
                while i < j and dist(j) > pivot: j -= 1
                points[i], points[j] = points[j], points[i]

            if K <= i - oi + 1:
                work(oi, i, K)
            else:
                work(i+1, oj, K - (i - oi + 1))

        work(0, len(points) - 1, K)
        return points[:K]

def kClosest(self, points, K):
        #use the
        #10,8,4
        #Need max heap but python provides min heap solution use -ve sign
        #Use the max heap

        import heapq
        hq = []
        op = []
        for i,j in points :
            rst = i**2 + j**2
            heapq.heappush(hq, [-rst, (i,j)])
            if(len(hq) > K) :
                heapq.heappop(hq)

        while(hq) :
            op += [ heapq.heappop(hq)[1] ]

        return op

def kClosest(self, points, K):
  return heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)


#Java sort w/ comparator
public int[][] kClosest(int[][] points, int K) {
    Arrays.sort(points, Comparator.comparing(p -> p[0] * p[0] + p[1] * p[1]));
    return Arrays.copyOfRange(points, 0, K);
}

#Java sort w/ lambda
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        Arrays.sort(points, (a,b) -> {
            Double ad = new Double(Math.sqrt(Math.pow((double)a[0], 2) + Math.pow((double)a[1], 2)));
            Double bd = new Double(Math.sqrt(Math.pow((double)b[0], 2) + Math.pow((double)b[1], 2)));
            return ad.compareTo(bd);
        });

        return Arrays.copyOfRange(points, 0, K);
    }
}

#We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
#(Here, the distance between two points on a plane is the Euclidean distance.)
#You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
#
#Example 1:
#Input: points = [[1,3],[-2,2]], K = 1
#Output: [[-2,2]]
#Explanation:
#The distance between (1, 3) and the origin is sqrt(10).
#The distance between (-2, 2) and the origin is sqrt(8).
#Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
#We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
#Example 2:
#Input: points = [[3,3],[5,-1],[-2,4]], K = 2
#Output: [[3,3],[-2,4]]
#(The answer [[-2,4],[3,3]] would also be accepted.)
#
#Note:
#    1 <= K <= points.length <= 10000
#    -10000 < points[i][0] < 10000
#    -10000 < points[i][1] < 10000
