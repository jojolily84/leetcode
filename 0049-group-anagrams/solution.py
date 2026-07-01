from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)  
        #defaultdict(list)第一次存取不存在的 key時，不會KeyError，直接自動建立空[]，所以不需要先判斷key是否存在。
        for s in strs:
            # key: 26 字母出現次數的 tuple，作為 canonical form
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1  #把字母轉成 0~25 的索引
            key = tuple(count)
            groups[key].append(s)
        return list(groups.values())
