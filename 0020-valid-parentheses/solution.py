class Solution:
    def isValid(self, s: str) -> bool:
        #用一個 dict 把「右括號 → 對應左括號」的映射存起來
        stack = []  #用來存放尚未配對的左括號
        pairs = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in pairs:  # 右括號
                if not stack or stack[-1] != pairs[char]:  #目前 stack 最上面!=目前這個右括號 char 對應的正確左括號
                    return False
                stack.pop()  #stack and stack[-1] == pairs[char]
            else:  # 左括號
                stack.append(char)
        return not stack  #最後檢查 stack 是否還有殘留
