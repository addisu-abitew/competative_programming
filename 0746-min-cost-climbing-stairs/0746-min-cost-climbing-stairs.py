class Solution:
    def minCostClimbingStairs(self, cost: List[int], i = -1, mem={}) -> int:
        if i+2 >= len(cost):
            mem[i] = 0
            return 0
        if i+1 not in mem: mem[i+1] = self.minCostClimbingStairs(cost, i+1, mem)
        if i+2 not in mem: mem[i+2] = self.minCostClimbingStairs(cost, i+2, mem)
        if i not in mem: mem[i] = min(cost[i+1]+mem[i+1], cost[i+2]+mem[i+2])
        res = mem[i]
        if i == -1: mem.clear()
        return res