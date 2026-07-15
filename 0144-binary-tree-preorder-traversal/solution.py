#Preorder 順序：Root → Left → Right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
    
        #iterative
#        if not root:
#            return []
#        res = []
#        stack = [root]
#        while stack:
#            node = stack.pop()
#            res.append(node.val)
#            if node.right:
#                stack.append(node.right)
#            if node.left:
#                stack.append(node.left)
#        return res
