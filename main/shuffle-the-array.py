class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled = []
        for i in range(n):
            shuffled += [nums[i], nums[n+i]]
        return shuffled