# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
        dfs(root)
        return result

        #iterative-反轉法:Postorder (L→R→Root) 反過來是 Root→R→L
#        if not root:
#            return []
#        result = []
#        stack = [root]
#        while stack:
#            node = stack.pop()
# 先用 Root -> Right -> Left 的順序收集
#            result.append(node.val)  
#            if node.left:
#                stack.append(node.left)
#            if node.right:
#                stack.append(node.right)
#        return result[::-1]
