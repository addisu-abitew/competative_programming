class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)
        ans = []
        for c in candies:
            ans.append(max_c - c <= extraCandies)
        return ans