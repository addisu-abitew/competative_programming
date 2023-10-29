class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        last_swap_i = len(heights)
        for i in range(len(heights)):
            for j in range(last_swap_i-1):
                if heights[j] < heights[j+1]:
                    names[j], names[j+1] = names[j+1], names[j]
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    last_swap_i = j+1
        return names