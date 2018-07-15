
#Path Sum III
#You are given a binary tree in which each node contains an integer value.
#Find the number of paths that sum to a given value.
#The path does not need to start or end at the root or a leaf, but it must go
#downwards (traveling only from parent nodes to child nodes).
#The tree has no more than 1,000 nodes and the values are in the range
#-1,000,000 to 1,000,000.
#Example:
#root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#      10
#     /  \
#    5   -3
#   / \    \
#  3   2   11
# / \   \
#3  -2   1
#Return 3. The paths that sum to 8 are:
#1.  5 -> 3
#2.  5 -> 2 -> 1
#3. -3 -> 11

## Two sum method
# Dict [sum] = # of paths
## Worst case - O(N)
# Space - O(N)
#Replica of Maximum size subarray sum
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        self.count = 0
        preDict = {0: 1}
        def dfs(p, target, pathSum, preDict):
            if p:
                pathSum += p.val
                self.count += preDict.get(pathSum - target, 0)
                preDict[pathSum] = preDict.get(pathSum, 0) + 1
                dfs(p.left, target, pathSum, preDict)
                dfs(p.right, target, pathSum, preDict)
                preDict[pathSum] -= 1
        dfs(root, target, 0, preDict)
        return self.count

#Remove pathSum as a parameter
class Solution(object):

    def pathSum(self, root, sum):
        dic = {0: 1}
        self.ans = 0

        def dfs(r, d, s):
            self.ans += d.get( s - sum, 0)
            d[s] = d.get( s, 0) + 1
            if r.left:
                dfs(r.left, d, s + r.left.val)
            if r.right:
                dfs(r.right, d, s + r.right.val)
            d[s] -= 1
        if not root:
            return 0
        dfs(root, dic, root.val)
        return self.ans

## Worst case - O(N^2)
class Solution(object):

    def pathSum(self, root, sum):
        if not root:
            return 0

        def pathSumFrom(root, sum) :
            if(not root) : return 0
            return ( 1 if sum == root.val else 0) + pathSumFrom(root.left, sum - root.val) +
pathSumFrom(root.right, sum - root.val)
            return int(sum == root.val) + pathSumFrom(root.left, sum - root.val) +
pathSumFrom(root.right, sum - root.val)


        return pathSumFrom(root , sum) + self.pathSum(root.left , sum) + self.pathSum(root.right,
sum);

#Analysis
#T: O(n^2) ,  O(nlogn) in best case (balanced tree).
#S : O(n)

#
#            1
#      2           3
#   4     5     6     7

#Analysis of pathSum
#Firstly, pathSum() will be called O(n) times, which is O(n) to traverse the
#tree.
#Analysis of pathSumFrom
#Then, on every node, we call pathSumFrom(), but notice, the time of this call
#is different on different node.
#Consider node 2 and node 3 in above tree, they have O(3) and O(3)
#respectfully. Which means,
#the sum time of pathSumFrom() from a layer is <= O(n).
#Overall, the time complexity is: O(n) + height * O(n)
#Best case = O(n) + logn * O(n) = O(nlogn)
#Worst case = O(n) + n * O(n) = O(n^2)

