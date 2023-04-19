class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        j = 0
        nums = '0123456789'
        while j < len(s):
            if s[j] == '[':
                n = j-1
                while n >= 0 and s[n] in nums:
                    n -= 1
                stack.append((s[n+1:j], j))
            elif s[j] == ']':
                n, i = stack.pop()
                w = s[i+1:j]
                s = s[:i-len(n)]+ (int(n)*w) + s[j+1:]
                print(s)
                j = j - 2 + (len(n)-1)*len(w) - len(n)
            j += 1
        return s