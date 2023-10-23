class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l, r = 0, len(plants)-1
        fill = 0
        curA, curB = capacityA, capacityB
        while l <= r:
            if l == r:
                if curA >= curB:
                    cur = plants[l]
                    if curA < cur:
                        fill += 1
                        curA = capacityA - cur
                    else:
                        curA -= cur
                elif curA < curB:
                    cur = plants[r]
                    if curB < cur:
                        fill += 1
                        curB = capacityB - cur
                    else:
                        curB -= cur
            else:
                curL, curR = plants[l], plants[r]
                
                if curA < curL:
                    fill += 1
                    curA = capacityA - curL
                else:
                    curA -= curL
                    
                if curB < curR:
                    fill += 1
                    curB = capacityB - curR
                else:
                    curB -= curR
            l += 1
            r -= 1
        return fill