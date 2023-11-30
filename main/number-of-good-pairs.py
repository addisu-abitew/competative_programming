class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        counter = Counter()
        for num in nums:
            pairs += counter[num]
            counter[num] += 1
        return pairs