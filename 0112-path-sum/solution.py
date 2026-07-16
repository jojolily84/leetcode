#把targetSum沿路徑往下傳遞時，用「減法」取代「加法」每到一個節點就扣掉該節點的值，抵達 leaf 時檢查剩餘值是否等於 0。
#邊界條件是本題的關鍵陷阱：
#root is None 要回傳 False（空樹沒有 path），但單一節點若剛好等於 target 要回傳 True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # leaf node：檢查剩餘 target 是否=這個節點值
        if not root.left and not root.right:
            return targetSum == root.val
        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining) or
                self.hasPathSum(root.right, remaining))
