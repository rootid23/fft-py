
class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0
        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow) #Go thru root
            return max(left_arrow, right_arrow) #Not go thru root
        arrow_length(root)
        return self.ans
#child-Parent-child order, where not necessarily be parent-child order.
#Longet increasing sequnce (Must be from parent to child)

private int maxLength = 0;
public int longestConsecutive(TreeNode root) {
    dfs(root);
    return maxLength;
}
private int dfs(TreeNode p) {
    if (p == null) return 0;
    int L = dfs(p.left) + 1;
    int R = dfs(p.right) + 1;
    if (p.left != null && p.val + 1 != p.left.val) {
        L = 1;
    }
    if (p.right != null && p.val + 1 != p.right.val) {
        R = 1;
    }
    int length = Math.max(L, R);
    maxLength = Math.max(maxLength, length);
    return length;
}

#Longest Univalue Path
#Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
#Note: The length of path between two nodes is represented by the number of edges between them.
#Example 1:
#Input:
#              5
#             / \
#            4   5
#           / \   \
#          1   1   5
#Output:
#2
#Example 2:
#Input:
#              1
#             / \
#            4   5
#           / \   \
#          4   4   5
#Output:
#2
