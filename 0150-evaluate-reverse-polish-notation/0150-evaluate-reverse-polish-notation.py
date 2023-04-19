class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        while i < len(tokens):
            if tokens[i] in '+-*/':
                if tokens[i] == '+':
                    tokens[i-2] = str(int(tokens[i-2]) + int(tokens[i-1]))
                if tokens[i] == '-':
                    tokens[i-2] = str(int(tokens[i-2]) - int(tokens[i-1]))
                if tokens[i] == '*':
                    tokens[i-2] = str(int(tokens[i-2]) * int(tokens[i-1]))
                if tokens[i] == '/':
                    res = int(tokens[i-2]) // int(tokens[i-1])
                    if res<0 and (int(tokens[i-2]) % int(tokens[i-1])):   res += 1
                    tokens[i-2] = str(res)
                tokens.pop(i-1)
                tokens.pop(i-1)
                i -= 1
            else:
                i += 1
        return int(tokens[0])