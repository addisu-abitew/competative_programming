class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                stack.append(i)
                i += 1
            elif s[i] == ')':
                lp = stack.pop()
                l = s[:lp]
                rev = s[lp+1:i][::-1]
                r = s[i+1:]
                s = l + rev + r
                i -= 1
            else:
                i += 1
        return s