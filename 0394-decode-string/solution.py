#後進先出、遇到結束符號才回頭處理，是典型的 stack
"""只要問題具有「進入子層級 → 子層級處理完 → 退回上一層」的遞迴式結構，
且「上一層」永遠是指「最近一次尚未結束的那層」，就是 stack（或等價的 recursion，
因為 recursion 本身就是靠 call stack 實現的）。"""

class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []  #存還沒用到的數字(k)
        str_stack = []  #存進入[之前，外層已經累積的字串
        current_str = ""
        k = 0
        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                # 進入新的一層，先把現在的狀態存起來
                num_stack.append(k)
                str_stack.append(current_str)
                current_str = ""
                k = 0
            elif char == ']':
                # 這一層結束，回到上一層並套用倍數
                prev_str = str_stack.pop()
                repeat_k = num_stack.pop()
                current_str = prev_str + current_str * repeat_k
            else:
                current_str += char
        return current_str
