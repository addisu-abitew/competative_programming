class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arranged = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i] != arranged[i]:
                ans += 1
        return ans