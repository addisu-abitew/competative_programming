class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        last_swap_i = len(heights)-1
        
        for i in range(len(heights)):
            swapped = False
            for j in range(last_swap_i):
                if heights[j] < heights[j+1]:
                    names[j], names[j+1] = names[j+1], names[j]
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    last_swap_i = j
                    swapped = True
            if not swapped:
                return names
        return names