class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        presum = [0]
        for num in gain:
            presum.append(presum[-1] + num)
        return max(presum)