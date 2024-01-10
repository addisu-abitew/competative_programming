class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        recolors = 0
        minimum_recolors =len(blocks)
        l=0
        
        for r in range(len(blocks)):
            if blocks[r]=="W":
                recolors+=1
            if r>=k-1:
                minimum_recolors = min(recolors,minimum_recolors)
                if blocks[l]=="W":
                    recolors-=1
                l+=1
        return minimum_recolors
                