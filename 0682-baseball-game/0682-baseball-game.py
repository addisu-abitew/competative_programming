class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == '+' and len(stack) > 1:
                stack.append(stack[-1] + stack[-2])
            elif operation == 'D' and stack:
                stack.append(stack[-1]*2)
            elif operation == 'C' and stack:
                stack.pop()
            else:
                stack.append(int(operation))
        print(stack)
        return sum(stack)