class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts = Counter(s)
        stack = []
        visited = set()
        for val in s:
            if val in visited:
                counts[val] -= 1
            else:
                while stack and stack[-1] > val and counts[stack[-1]] > 1:
                    removed = stack.pop()
                    counts[removed] -= 1
                    visited.remove(removed)
                visited.add(val)
                stack.append(val)
        return ''.join(stack)