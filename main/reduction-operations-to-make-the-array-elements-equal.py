class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ops = 0
        counter = Counter(nums)
        dist_nums = sorted(list(set(nums)))
        for i, num in enumerate(dist_nums):
            ops += i*counter[num]
        return ops