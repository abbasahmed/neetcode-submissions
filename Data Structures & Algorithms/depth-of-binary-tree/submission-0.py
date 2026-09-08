# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthRec(root, 0)

    def maxDepthRec(self, root, d):
        if root is None:
            return d
        leftdepth = self.maxDepthRec(root.left, d + 1)
        rightdepth = self.maxDepthRec(root.right, d + 1)
        return max(leftdepth, rightdepth)

            
        