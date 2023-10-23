class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l, r = 0, len(plants)-1
        fill = 0
        curA, curB = capacityA, capacityB
        while l < r:
            curL, curR = plants[l], plants[r]
            if curA < curL:
                fill += 1
                curA = capacityA
            if curB < curR:
                fill += 1
                curB = capacityB
            curA -= curL
            curB -= curR
            l += 1
            r -= 1
        
        if l == r and (max(curA, curB) < plants[l]):
            fill += 1
        return fill