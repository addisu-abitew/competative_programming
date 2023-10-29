class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for operation in logs:
            if operation == '../':
                if stack:
                    stack.pop()
            elif operation != './':
                stack.append(operation)
        print(stack)
        return len(stack)