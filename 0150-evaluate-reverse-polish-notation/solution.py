class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operator:
                b = stack.pop()  #右運算元
                a = stack.pop()  #左運算元
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a/b))  #往0靠近
            else:
                stack.append(int(token))
        return stack[0]  #回傳數值
