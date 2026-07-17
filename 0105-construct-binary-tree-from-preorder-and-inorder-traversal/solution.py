# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {val: i for i, val in enumerate(inorder)}
        self.preorder_index = 0
        
        def build(inorder_left: int, inorder_right: int) -> TreeNode | None:
            if inorder_left > inorder_right:
                return None
            
            root_val = preorder[self.preorder_index]
            root = TreeNode(root_val)
            self.preorder_index += 1
            
            mid = inorder_index_map[root_val]
            # preorder 順序是 root -> left -> right，左子樹必須先建
            root.left = build(inorder_left, mid - 1)
            root.right = build(mid + 1, inorder_right)
            return root
        return build(0, len(inorder) - 1)
