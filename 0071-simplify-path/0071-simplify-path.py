class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        arr = path.split('/')
        for val in arr:
            if val == '..':
                if stack: stack.pop()
            elif not(val == '' or val == '.'):
                stack.append(val)
        return '/'+'/'.join(stack)