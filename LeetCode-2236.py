# https://leetcode.com/problems/root-equals-sum-of-children/
"""
2236. Root Equals Sum of Children

You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.

Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.


Example 1:
Input: root = [10,4,6]
Output: true
Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
10 is equal to 4 + 6, so we return true.

Example 2:
Input: root = [5,3,1]
Output: false
Explanation: The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
5 is not equal to 3 + 1, so we return false.


Constraints:
The tree consists only of the root, its left child, and its right child.
-100 <= Node.val <= 100
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def fill_tree(lst: list) -> TreeNode:
    tn = TreeNode()
    tn.val = lst[0]
    tn.left = TreeNode(val=lst[1])
    tn.right = TreeNode(val=lst[2])
    return tn

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val+root.right.val
        
if __name__ == '__main__':
    root = [5,3,1]
    print(f"root:{root}")
    print(f"output:{Solution().checkTree(fill_tree(root))}")