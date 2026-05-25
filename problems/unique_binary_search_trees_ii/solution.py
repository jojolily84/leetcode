# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        def build(l, r):
            if l > r:
                return [None]
            res = []
            for i in range(l, r + 1):
                leftTrees = build(l, i - 1)
                rightTrees = build(i + 1, r)
                for L in leftTrees:
                    for R in rightTrees:
                        root = TreeNode(i)
                        root.left = L
                        root.right = R
                        res.append(root)
            return res
        return build(1,n)