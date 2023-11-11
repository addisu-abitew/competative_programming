class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for val in pushed:
            stack.append(val)
            while popped and popped[0] in stack:
                stack.pop()
                popped.pop(0)
        return len(stack) == 0