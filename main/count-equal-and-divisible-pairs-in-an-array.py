class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pos = defaultdict(set)
        pairs = 0
        for i in range(len(nums)):
            for j in pos[nums[i]]:
                if i*j % k == 0:
                    pairs += 1
            pos[nums[i]].add(i)
        return pairs