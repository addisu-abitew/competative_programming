class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_val = nums[0]
        stack = []
        for val in nums[1:]:
            while stack and stack[-1][0] <= val:
                stack.pop()
            if stack and stack[-1][1] < val:
                return True
            stack.append([val, min_val])
            min_val = min(val, min_val)
        return False