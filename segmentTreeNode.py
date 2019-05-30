#https://en.wikipedia.org/wiki/Range_searching
#https://stackoverflow.com/questions/28470692/how-is-the-memory-of-the-array-of-segment-tree-2-2-ceillogn-1
#3 ways
#1. w/ arrays
#2. w/ tree
#3. w/ array + bits
#https://leetcode.com/problems/range-sum-query-mutable/discuss/75753/Java-using-Binary-Indexed-Tree-with-clear-explanation
#https://visualgo.net/en/segmenttree
class SegmentTreeNode:

  #range (start, end, refrences to left and right)
  def __init__(self, start, end, val, left=None, right=None):
    self.start = start
    self.end = end
    self.mid = start + (end - start) // 2
    self.val = val
    self.left = left
    self.right = right

class NumArray:
  def __init__(self, nums):
    self.nums = nums
    if self.nums:
      self.root = self._buildTree(0, len(nums) - 1)

  def update(self, i, val):
    self._updateTree(self.root, i, val)

  def sumRange(self, i, j):
    return self._sumRange(self.root, i, j)


  def _buildTree(self, start, end):
    if start == end:
      #create
      return SegmentTreeNode(start, end, self.nums[start])
    mid = start + (end - start) // 2
    left = self._buildTree(start, mid)
    right = self._buildTree(mid + 1, end)

    #Merge the result
    return SegmentTreeNode(start, end, left.val + right.val, left, right)

  def _updateTree(self, root, i, val):
    if root.start == i and root.end == i:
      root.val = val
      return
    if i <= root.mid:
      self._updateTree(root.left, i, val)
    else:
      self._updateTree(root.right, i, val)

    #Merge the result
    root.val = root.left.val + root.right.val

  def _sumRange(self, root, i, j):
    if root.start == i and root.end == j:
      return root.val
    #Filter
    if j <= root.mid:
      return self._sumRange(root.left, i, j)
    elif i > root.mid:
      return self._sumRange(root.right, i, j)
    #Merge the result
    return self._sumRange(root.left, i, root.mid) + self._sumRange(root.right, root.mid + 1, j)





class NumArray(object):

	def __init__(self, nums):
		self.l = len(nums)
		self.tree = [0]*self.l + nums
		for i in range(self.l - 1, 0, -1):
			self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]

	def update(self, i, val):
		n = self.l + i
		self.tree[n] = val
		while n > 1:
			self.tree[n>>1] = self.tree[n] + self.tree[n^1]
			n >>= 1


	def sumRange(self, i, j):
		m = self.l + i
		n = self.l + j
		res = 0
		while m <= n:
			if m & 1:
				res += self.tree[m]
				m += 1
			m >>= 1
			if n & 1 ==0:
				res += self.tree[n]
				n -= 1
			n >>= 1
		return res


#https://leetcode.com/articles/range-sum-query-mutable/#
int[] tree;
int n;
public NumArray(int[] nums) {
    if (nums.length > 0) {
        n = nums.length;
        tree = new int[n * 2];
        buildTree(nums);
    }
}
private void buildTree(int[] nums) {
    for (int i = n, j = 0;  i < 2 * n; i++,  j++)
        tree[i] = nums[j]; #Build leaf
    for (int i = n - 1; i > 0; --i)
        tree[i] = tree[i * 2] + tree[i * 2 + 1];
}

# Update bottom up
void update(int pos, int val) {
    pos += n;
    tree[pos] = val;
    while (pos > 0) {
        int left = pos;
        int right = pos;
        if (pos % 2 == 0) {
            right = pos + 1;
        } else {
            left = pos - 1;
        }
        // parent is updated after child is updated
        tree[pos / 2] = tree[left] + tree[right];
        pos /= 2;
    }
}

#query
public int sumRange(int l, int r) {
    // get leaf with value 'l'
    l += n;
    // get leaf with value 'r'
    r += n;
    int sum = 0;
    while (l <= r) {
        if ((l % 2) == 1) {
           sum += tree[l];
           l++;
        }
        if ((r % 2) == 0) {
           sum += tree[r];
           r--;
        }
        l /= 2;
        r /= 2;
    }
    return sum;
}
