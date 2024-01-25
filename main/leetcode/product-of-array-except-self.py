class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = nums.count(0)
        answer = [0 for _ in range(n)]
        if zeros > 1: return answer
        
        prod = 1
        for num in nums:
            prod *= num if num != 0 else 1
        if zeros == 1:
            zi = nums.index(0)
            answer[zi] = prod
        else:
            answer = [prod//num for num in nums]
        return answer