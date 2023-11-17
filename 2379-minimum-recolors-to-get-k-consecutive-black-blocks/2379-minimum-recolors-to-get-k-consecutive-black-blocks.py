class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minRecolor = float('inf')
        recolor = 0
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                recolor += 1
            if r >= k and blocks[r-k] == 'W':
                recolor -= 1
            if r >= k-1:
                minRecolor = min(minRecolor, recolor)
        return minRecolor