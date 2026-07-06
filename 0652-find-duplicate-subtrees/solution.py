# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = defaultdict(int)
        result = []
        def serialize(node):
            if not node:
                return "#"
            key = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            count[key] += 1
            if count[key] == 2:  # 第一次出現重複時才加入
                result.append(node)
            return key
        serialize(root)
        return result
