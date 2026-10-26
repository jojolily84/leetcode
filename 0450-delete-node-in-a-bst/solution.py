# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None
        
        if key <root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 一個節點
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # 兩個節點，找右子樹最小值(左節點)取代
            node = root.right
            while node.left:
                node = node.left
            
            root.val = node.val
            root.right = self.deleteNode(root.right, node.val)
            
        return root
