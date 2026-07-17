# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}  #從inorder 找 root 在 inorder 中的位置
        self.post_idx = len(postorder) - 1  #指向 postorder 陣列的尾端
        
        def build(left: int, right: int) -> Optional[TreeNode]:
            # left 和 right 是 inorder 陣列的 index 範圍
            if left > right:
                return None
            
            # postorder最後一個元素永遠是當前這整棵樹的 root
            #在目前這一段 postorder 範圍裡，最後一個值就是這一段所對應的 subtree 的 root
            root_val = postorder[self.post_idx]
            root = TreeNode(root_val)
            self.post_idx -= 1  #指標往前移一格
            
            # postorder 從尾巴往前取，必須先建 right 再建 left
            # index 從 idx_map[root_val]+1 到 right -> 全部屬於 right subtree
            root.right = build(idx_map[root_val] + 1, right)
            # index 從 left 到 idx_map[root_val]-1 -> 全部屬於 left subtree
            root.left = build(left, idx_map[root_val] - 1)
            
            return root
        return build(0, len(inorder) - 1)
